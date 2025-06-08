from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models import User, Task
from app.forms import RegistrationForm, LoginForm, TaskForm
from datetime import datetime

main = Blueprint('main', __name__)
auth = Blueprint('auth', __name__)

@main.route('/')
@main.route('/index')
@login_required
def index():
    tasks = Task.query.filter_by(user_id=current_user.id).order_by(Task.due_date.asc()).all()
    return render_template('index.html', title='Home', tasks=tasks)

@main.route('/task/new', methods=['GET', 'POST'])
@login_required
def new_task():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(
            title=form.title.data,
            description=form.description.data,
            due_date=form.due_date.data,
            priority=form.priority.data,
            status=form.status.data,
            user_id=current_user.id
        )
        db.session.add(task)
        db.session.commit()
        flash('Your task has been created!', 'success')
        return redirect(url_for('main.index'))
    return render_template('create_task.html', title='New Task', form=form)

@main.route('/task/<int:task_id>/update', methods=['GET', 'POST'])
@login_required
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.user_id != current_user.id:
        abort(403)
    form = TaskForm()
    if form.validate_on_submit():
        task.title = form.title.data
        task.description = form.description.data
        task.due_date = form.due_date.data
        task.priority = form.priority.data
        task.status = form.status.data
        db.session.commit()
        flash('Your task has been updated!', 'success')
        return redirect(url_for('main.index'))
    elif request.method == 'GET':
        form.title.data = task.title
        form.description.data = task.description
        form.due_date.data = task.due_date
        form.priority.data = task.priority
        form.status.data = task.status
    return render_template('update_task.html', title='Update Task', form=form)

@main.route('/task/<int:task_id>/delete', methods=['POST'])
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.user_id != current_user.id:
        abort(403)
    db.session.delete(task)
    db.session.commit()
    flash('Your task has been deleted!', 'success')
    return redirect(url_for('main.index'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html', title='Register', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid email or password', 'danger')
            return redirect(url_for('auth.login'))
        login_user(user)
        next_page = request.args.get('next')
        return redirect(next_page or url_for('main.index'))
    return render_template('login.html', title='Sign In', form=form)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index')) 