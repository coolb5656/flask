from crypt import methods
from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db

reserve = Blueprint('reserve', __name__)

@reserve.route("add", methods=["GET", "POST"]) # reserve items
def reserve():
    # TODO add reservation logic
    pass

@reserve.route("change", methods=["GET", "POST"]) # change reservation
def checkin():
    # TODO change reservation logic
    pass

@reserve.route("delete", methods=["POST"]) # delete reservation
def scam():
    # TODO delete reservation logic
    pass