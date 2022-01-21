from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db
from flask_login import login_required, current_user


main = Blueprint('main', __name__)

@main.route("/profile")
@login_required
def profile():
    return render_template("views/profile.html", name=current_user.name)

@main.route("/items") # view all items
def items():
    # TODO items view logic
    pass

@main.route("/item/<id>") # view item
def item(id):
    # TODO item view logic
    pass

@main.route("/students") # view all students
def students():
    # TODO students view logic
    pass

@main.route("/student/<id>") # view student
def student(id):
    # TODO student view logic
    pass

@main.route("/reservations") # view all reservations
def reservations():
    # TODO reservations view logic
    pass

@main.route("/reservation/<id>") # view reservation
def reservation(id):
    # TODO reservation view logic
    pass