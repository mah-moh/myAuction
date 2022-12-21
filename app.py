from flask import Flask, render_template, url_for, request, redirect, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_session import Session

app = Flask(__name__)
app = Flask(__name__, template_folder='views/templates')
app.config['SECRET_KEY'] = 'your secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auction.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

import controllers

@app.route('/')
def home():
    return controllers.Handle_home()

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return controllers.Handle_signup()

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    return controllers.Handle_signin()

@app.route('/create_listing', methods=['GET', 'POST'])
def create_listing():
    return controllers.Handle_add_product()

@app.route('/my_bid')
def my_bid():
    return controllers.Handle_my_bid()

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

@app.route('/product/<int:id>', methods=['GET', 'POST'])
def product(id):
    return controllers.Handle_bidding(id)

@app.route('/product/delete/<int:id>', methods=['GET', 'POST'])
def delete_product(id):
    return controllers.Handle_delete_product(id)

@app.route('/profile')
def profile():
    return controllers.Handle_profile()

@app.route('/update', methods=['GET', 'POST'])
def update():
    return controllers.Handle_update()

if __name__ == '__main__':
    app.run(debug=True)