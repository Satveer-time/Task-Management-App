# Task Management Application

A full-stack web application built with Python Flask that demonstrates modern web development practices and clean architecture.

## 🚀 Features

### User Management
- Secure user authentication system
- User registration and login
- Password hashing and protection
- Session management

### Task Management
- CRUD operations for tasks
- Task prioritization (High, Medium, Low)
- Status tracking (Pending, In Progress, Completed)
- Due date management
- User-specific task lists

### Technical Features
- RESTful API architecture
- Database management with SQLAlchemy
- Form validation and error handling
- Responsive design with Bootstrap 5
- Flash messages for user feedback
- Modal confirmations for deletions

## 🛠️ Technologies Used

### Backend
- Python 3.x
- Flask (Web Framework)
- SQLAlchemy (ORM)
- Flask-Login (Authentication)
- Flask-WTF (Forms)
- Werkzeug (Security)

### Frontend
- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- Bootstrap Icons

### Database
- SQLite (Development)
- SQLAlchemy ORM

## 📋 Project Structure
```
task_manager/
├── app/
│   ├── __init__.py      # Application factory
│   ├── models.py        # Database models
│   ├── routes.py        # Route handlers
│   ├── forms.py         # Form classes
│   └── templates/       # HTML templates
├── migrations/          # Database migrations
├── instance/           # Instance-specific files
├── .env               # Environment variables
├── config.py          # Configuration
└── run.py            # Development server
```

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- pip (Python package manager)

### Installation

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

## 💻 Code Examples

### User Model
```python
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    tasks = db.relationship('Task', backref='author', lazy='dynamic')
```

### Task Model
```python
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    due_date = db.Column(db.DateTime)
    priority = db.Column(db.String(20), default='Medium')
    status = db.Column(db.String(20), default='Pending')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
```

## 🔒 Security Features
- Password hashing using Werkzeug
- CSRF protection
- Form validation
- Secure session management
- User authentication
- Protected routes

## 🎨 UI/UX Features
- Responsive design
- Card-based task display
- Priority-based color coding
- Status indicators
- Modal confirmations
- Form validation feedback
- Flash messages

## 📝 Future Improvements
- [ ] Add task categories
- [ ] Implement task search
- [ ] Add task filtering
- [ ] Email notifications
- [ ] Task sharing between users
- [ ] Dark mode support
- [ ] Mobile app version

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author
Satveer Singh

## 📞 Contact
Project Link: [https://github.com/Satveer-time/Task-Management-App](https://github.com/Satveer-time/Task-Management-App) 
