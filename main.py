# import Model.author as author
# import Model.book as book
from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'cac873583f189291c68823d86860459a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable = False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable= False)
    used_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.title}', '{self.date_posted}')"




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
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('hello'))
    return render_template('register.html', title='Registration', form = form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'new' and form.password.data == '123':
            flash(f'Logged {form.username.data} successfully!', 'success')
            return redirect(url_for('hello'))
        else:
            flash('Something wrong with your password', 'danger')
    return render_template('login.html', title='Login Page', form = form)

# @app.route('/<name>')
# def hello_name(name):
#     return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run(debug=True)



# author1 = author.authorClass("anish", 25)
# book1 = book.book(123, "Named", author1)

# book1 = book(123,"Bio of Anish", author1)
# author1.printAuthor()
# book1.printBook()

# if __name__ == "__main__":
    # name,age = input("Enter Name and Age").split()
    # # print("Hello")
    # author1 = author.authorClass(name,age)
    # isbn,bookName = input("Enter Name and Age").split()
    # # print("Hello")
    # author1 = author.authorClass(name,age)
    # book1 = book.book(isbn,bookName,author1)
    # print(book1.authorList.name)

    # books = []
    # author = [] 

    # for k in range(3):


    # for i in range(3):

    #     newBook = book.book(i,"Bio" + str(i), "Anish")
    #     books.append(newBook)

    # for j in range(3):
    #     print(books[j].nameOfBook)







