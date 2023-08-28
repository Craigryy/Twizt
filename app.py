from flask import Flask, render_template, request, redirect
from flask_pymongo import PyMongo
from bson import ObjectId  # Import ObjectId from bson module

app = Flask(__name__, template_folder='templates')
app.config["MONGO_URI"] = "mongodb://localhost:27017/todo"
mongo = PyMongo(app)

@app.route('/')
def index():
    tasks = mongo.db.tasks.find()
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task_description = request.form.get('task_description')
    mongo.db.tasks.insert_one({'description': task_description, 'completed': False})
    return redirect('/')

@app.route('/update_task/<task_id>', methods=['POST'])
def update_task(task_id):
    task = mongo.db.tasks.find_one({'_id': ObjectId(task_id)})  # Convert task_id to ObjectId
    new_status = not task['completed']
    mongo.db.tasks.update_one({'_id': ObjectId(task_id)}, {'$set': {'completed': new_status}})
    return redirect('/')

@app.route('/delete_task/<task_id>', methods=['POST'])
def delete_task(task_id):
    mongo.db.tasks.delete_one({'_id': ObjectId(task_id)})  # Convert task_id to ObjectId
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
