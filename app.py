from flask import Flask, render_template, request, redirect
from bson import ObjectId
from pymongo import MongoClient
from dotenv import dotenv_values

# Create a Flask web application instance
app = Flask(__name__, template_folder='templates', static_folder='static')

# Load environment variables from the .env file
config = dotenv_values(".env")

# Establish a connection to the MongoDB cluster using the URI from .env
mongodb_uri = config["ATLAS_URI"]

try:
    client = MongoClient(mongodb_uri)
    # Access a specific database from .env
    db = client[config["DB_NAME"]]
    print("Connected to the MongoDB database!")
except Exception as e:
    print("Failed to connect to the MongoDB database:", str(e))

# Define a route for the homepage ("/")
@app.route('/')
def index():
    # Retrieve tasks from the MongoDB database
    tasks = db.tasks.find()
    # Render the "index.html" template with the tasks
    return render_template('index.html', tasks=tasks)

# Define a route for adding tasks ("/add_task")
@app.route('/add_task', methods=['POST'])
def add_task():
    # Get the task description from the form submitted via POST
    task_description = request.form.get('task_description')
    # Insert the task into the MongoDB database
    db.tasks.insert_one({'description': task_description, 'completed': False})
    # Redirect back to the homepage
    return redirect('/')

# Define a route for updating task completion status ("/update_task/<task_id>")
@app.route('/update_task/<task_id>', methods=['POST'])
def update_task(task_id):
    # Find the task in the MongoDB database using the task_id (converted to ObjectId)
    task = db.tasks.find_one({'_id': ObjectId(task_id)})
    # Toggle the completion status of the task
    new_status = not task['completed']
    # Update the task's completion status in the database
    db.tasks.update_one({'_id': ObjectId(task_id)}, {'$set': {'completed': new_status}})
    # Redirect back to the homepage
    return redirect('/')

# Define a route for deleting a task ("/delete_task/<task_id>")
@app.route('/delete_task/<task_id>', methods=['POST'])
def delete_task(task_id):
    # Delete the task from the MongoDB database using the task_id (converted to ObjectId)
    db.tasks.delete_one({'_id': ObjectId(task_id)})
    # Redirect back to the homepage
    return redirect('/')

# Run the Flask app only if the script is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
