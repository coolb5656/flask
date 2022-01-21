from crypt import methods
from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db

checkout = Blueprint('checkout', __name__)

@checkout.route("checkout", methods=["GET", "POST"]) # checkin items
def checkout():
    # TODO checkout logic
    pass

@checkout.route("checkin", methods=["GET", "POST"]) # checkout items
def checkin():
    # TODO checkin logic
    pass

@checkout.route("scan", methods=["POST"]) # backend for returnig item names
def scam():
    # TODO scan logic
    pass