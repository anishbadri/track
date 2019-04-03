from flask import render_template, url_for, flash, redirect
from track.forms import RegistrationForm, LoginForm
from track import app, bcrypt, db
from track.models import User, Post
from flask_login import login_user, current_user, logout_user



books = [
    {
        "title": "When Breathe becomes air",
        "author": "Paul Kalanidhi"
    },
    {
        "title": "Flow",
        "author": "Mihaly"
    }
]

@app.route('/')
def hello():
    return render_template('home.html', books=books)

# @app.route('/about')
# def about():
#     return render_template('about.html', title = 'About')

@app.route('/register', methods=['GET', 'POST'])
def registration():
    if current_user.is_authenticated:
        return redirect(url_for('hello'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('UTF-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        flash(f'Your account has been successfully created !', 'success')
        return redirect(url_for('hello'))
    return render_template('register.html', title='Registration', form = form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('hello'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Successfully logged in', 'Success')
            return redirect(url_for('hello'))
        else:
            flash('Something wrong with your password or email', 'danger')
    return render_template('login.html', title='Login Page', form = form)


    @app.route('/logout')
    def logout():
        logout_user()
        return redirect(url_for('home'))
