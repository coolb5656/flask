from crypt import methods
from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db

views = Blueprint('views', __name__)

@views.route("items") # view all items
def items():
    # TODO items view logic
    pass

@views.route("item/<id>") # view item
def item(id):
    # TODO item view logic
    pass

@views.route("students") # view all students
def students():
    # TODO students view logic
    pass

@views.route("student/<id>") # view student
def scam():
    # TODO student view logic
    pass

@views.route("reservations") # view all reservations
def reservations():
    # TODO reservations view logic
    pass

@views.route("reservation/<id>") # view reservation
def scam():
    # TODO reservation view logic
    pass