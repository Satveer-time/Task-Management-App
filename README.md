# Task Management Application

A modern task management application built with Python Flask, featuring user authentication, task creation, and management capabilities.

![Task Manager Screenshot](https://via.placeholder.com/800x400?text=Task+Manager+Screenshot)

## Live Demo
[View Live Application](https://your-render-app-url.onrender.com)

## Features

- **User Authentication**
  - Secure user registration and login
  - Password hashing and protection
  - User-specific task management

- **Task Management**
  - Create, read, update, and delete tasks
  - Task categorization and priority levels
  - Due date tracking
  - Status tracking (Pending, In Progress, Completed)

- **Modern UI/UX**
  - Responsive design with Bootstrap 5
  - Clean and intuitive interface
  - Card-based task display
  - Modal confirmations for deletions
  - Form validation
  - Flash messages for user feedback

## Technologies Used

- **Backend:**
  - Python 3.x
  - Flask (Web Framework)
  - SQLAlchemy (ORM)
  - Flask-Login (Authentication)
  - Flask-WTF (Forms)

- **Frontend:**
  - HTML5
  - CSS3
  - Bootstrap 5
  - JavaScript

- **Database:**
  - SQLite (Development)
  - PostgreSQL (Production)

- **Deployment:**
  - Render.com
  - Gunicorn (WSGI Server)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Satveer-time/Task-Management-App.git
   cd Task-Management-App
   ```

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

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Satveer Singh - [satveer3002@gmail.com]

Project Link: [https://github.com/Satveer-time/Task-Management-App](https://github.com/Satveer-time/Task-Management-App) 
