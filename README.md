# cs50project
# Task Management Application

This is a simple Task Management application built with Flask, 
SQLAlchemy, and Bootstrap. The application allows users to register,
log in, and manage their tasks (create, read, update, and delete). 
Each user has their own set of tasks, and only authenticated users can access the task management features.

## Features

- **User Authentication**: Users can register and log in to manage their tasks.
- **Task Management**: Users can create, view, update, and delete tasks.
- **Personalized Tasks**: Each user has their own tasks, which are securely managed through their account.
- **Responsive UI**: The application uses Bootstrap for a responsive and clean user interface.
- **Security**: Passwords are hashed using bcrypt for secure storage.

## Technologies Used

- **Python**: The backend is built using Flask.
- **Flask**: A micro web framework used for routing and handling HTTP requests.
- **SQLAlchemy**: ORM used for database interactions.
- **SQLite**: The database used to store user and task information.
- **Bootstrap**: Used for styling the frontend.
- **Jinja2**: Template engine for rendering HTML with dynamic data.
