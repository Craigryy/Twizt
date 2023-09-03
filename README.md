# Twizt

![todo](https://github.com/Craigryy/Twizt/assets/116971272/90170e57-a6f0-4e84-9bca-bddac3fb594d)


Twizt is a simple ToDo web application that helps users manage their tasks and keep track of their daily activities. It leverages the power of MongoDB as a NoSQL database to store and retrieve task-related data efficiently.


### Table of Contents

	•	Features
	•	Prerequisites
	•	Installation
	•	Usage
	•	Docker and Docker Compose

### Features

	1.	Add Tasks: Easily add new tasks to your to-do list with descriptions and completion status.
	2.	Update Tasks: Update the completion status of tasks to keep track of your progress.
	3.	Delete Tasks: Remove tasks that are no longer relevant or completed.
	4.	Persistent Data: All your tasks are stored in a MongoDB database for data persistence.

Prerequisites

Before you begin using Twizt, make sure you have the following installed on your system:

	•	Python 3.x
	•	Flask
	•	MongoDB
	•	Docker (optional)

Installation

	1. git clone https://github.com/Craigryy/twizt.git2. cd twizt
 Clone the Twist repository to your local machine




	2. pip install -r requirements.txt	
 
 Install the required Python packages using pip




	3.	Make sure your MongoDB server is running. Update the MongoDB connection settings in the config.py file if needed.

Usage

	1. python app.py
 
 Start the Flask application




	2.	Open your web browser and navigate to http://localhost:5000 to access the Twist app.
	3.	You can now use Twist to add, update, and delete tasks as needed.

Docker and Docker Compose

Twizt can also be run inside Docker containers for easy deployment and management. Docker Compose is used to define and run the services.

To run Twizt in Docker containers:

	1.	Ensure you have Docker and Docker Compose installed on your system.
	2.	Inside the Twist project directory, create a Docker Compose file (docker-compose.yml) with the following content:
 
``` console
version: '3'
services:
  twist:
    build: .
    ports:
      - "5000:5000"
    depends_on:
      - mongo
  mongo:
    image: mongo:latest
```


	3.	Build the Docker image and start the containers:
 
``` console 
docker-compose up --build
```


	4.	Open your web browser and navigate to http://localhost:5000 to access the Twist app running in a Docker container.

Now, Twizt is up and running in a Dockerized environment, making it easy to deploy and manage in various setups.

Twizt Task Management App on Heroku


App URL: https://intense-temple-95344-1fd564e3255b.herokuapp.com/

Features:

	•	Task Management: Users can add, update, and delete tasks.
	•	Persistent Data: Task data is stored in a MongoDB database, ensuring that tasks are saved even if the server restarts.

Usage:

	•	Users can access your app by visiting the provided Heroku URL https://intense-temple-95344-1fd564e3255b.herokuapp.com.
	•	They can start managing their tasks, benefiting from the task management features your app provides.

This deployment on Heroku makes your Twist app accessible to a wider audience, and users can conveniently use it without having to set up any infrastructure locally. It’s a great way to showcase your app to the world!
