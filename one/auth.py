from crypt import methods
from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        email = request.form.get("email")
        name = request.form.get("name")
        password = request.form.get("password")
        

        user = User.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password, password):
            flash("Wrong Email or Password!")
            return redirect(url_for("auth.login"))
        elif check_password_hash(user.password, password):
            return "Logged In!"
        

    return render_template('login.html', error=error)

@auth.route('/signup')
def signup():
    return render_template("auth/signup.html")

@auth.route('/signup', methods=["POST"])
def signup_post():
    email = request.form.get("email")
    name = request.form.get("name")
    password = request.form.get("password")

    user = User.query.filter_by(email=email).first()

    if user:
        flash('Email address already exists')
        return redirect(url_for("auth.signup"))

    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for("auth.login"))

@auth.route('/logout')
def logout():
    return 'Logout'