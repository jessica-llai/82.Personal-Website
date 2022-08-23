from flask import Flask, redirect,request, render_template, url_for
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from form import RegisterForm, LoginForm
from flask_bootstrap import Bootstrap
import os

# database & html stuffs
app = Flask(__name__)
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
db = SQLAlchemy(app)

# login
login_manager = LoginManager()
login_manager.init_app(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False, unique=True)

    def __repr__(self):
        return '<User %r>' % self.username

db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.route('/', methods=['GET','POST'])
def homepage():
    return render_template('index.html')

@app.route('/index.html')
def homepage2():
    return render_template('index.html')

@app.route('/work')
def elements():
    return render_template('work.html')

@app.route('/contact', methods=['GET','POST'])
def contact():
    return render_template('contact.html')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(
            name = form.name.data,
            email = form.email.data,
            password = form.password.data
        )


        db.session.add(new_user)
        db.session.commit()

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)




