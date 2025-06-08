# Task Management Application

A modern task management application built with Python Flask, featuring user authentication, task creation, and management capabilities.

## Features

- User authentication (signup, login, logout)
- Create, read, update, and delete tasks
- Task categorization and priority levels
- Due date tracking
- Responsive design with Bootstrap
- SQLite database for data persistence

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Initialize the database:
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```
5. Run the application:
   ```bash
   flask run
   ```

## Technologies Used

- Python 3.x
- Flask
- SQLAlchemy
- Flask-Login
- Bootstrap 5
- SQLite

## Project Structure

```
task_manager/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── forms.py
│   └── templates/
├── migrations/
├── instance/
├── .env
├── config.py
└── run.py
``` 