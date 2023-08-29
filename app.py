# Import necessary modules and classes
from flask import Flask, render_template, request, redirect
from flask_pymongo import PyMongo
from bson import ObjectId

# Create a Flask web application instance
app = Flask(__name__, template_folder='templates')

# Configure the MongoDB connection URI
app.config["MONGO_URI"] = "mongodb://localhost:27017/todo"

# Create a PyMongo instance using the Flask app
mongo = PyMongo(app)

# Define a route for the homepage ("/")
def index():
    # Retrieve tasks from the MongoDB database
    tasks = mongo.db.tasks.find()
    # Render the "index.html" template with the tasks
    return render_template('index.html', tasks=tasks)

# Define a route for adding tasks ("/add_task")
def add_task():
    # Get the task description from the form submitted via POST
    task_description = request.form.get('task_description')
    # Insert the task into the MongoDB database
    mongo.db.tasks.insert_one({'description': task_description, 'completed': False})
    # Redirect back to the homepage
    return redirect('/')

# Define a route for updating task completion status ("/update_task/<task_id>")
def update_task(task_id):
    # Find the task in the MongoDB database using the task_id (converted to ObjectId)
    task = mongo.db.tasks.find_one({'_id': ObjectId(task_id)})
    # Toggle the completion status of the task
    new_status = not task['completed']
    # Update the task's completion status in the database
    mongo.db.tasks.update_one({'_id': ObjectId(task_id)}, {'$set': {'completed': new_status}})
    # Redirect back to the homepage
    return redirect('/')

# Define a route for deleting a task ("/delete_task/<task_id>")
def delete_task(task_id):
    # Delete the task from the MongoDB database using the task_id (converted to ObjectId)
    mongo.db.tasks.delete_one({'_id': ObjectId(task_id)})
    # Redirect back to the homepage
    return redirect('/')


# Run the Flask app only if the script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
