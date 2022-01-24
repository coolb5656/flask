from datetime import datetime
from subprocess import check_call
from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db
from .models import item, reservation

import time
import atexit

from apscheduler.schedulers.background import BackgroundScheduler

reserve = Blueprint('reserve', __name__)

@reserve.route("add", methods=["GET", "POST"]) # reserve items
def add_reservation():
    # TODO add reservation logic
    pass

@reserve.route("change", methods=["GET", "POST"]) # change reservation
def edit_reservation():
    # TODO change reservation logic
    pass

@reserve.route("check") # WIP
def check_reservation():
    with db.app.app_context():
        reservations = reservation.query.all()

        for r in reservations:
            if r.date_out < datetime.now():
                i = item.query.filter_by(id=r.item_id).first()
                i.status="Reserved"
                i.student_id = r.student_id
                i.status_date = datetime.now()
                reservation.query.filter_by(id=r.id).delete()
                db.session.commit()


scheduler = BackgroundScheduler()
scheduler.add_job(func=check_reservation, trigger="interval", seconds=5)
scheduler.start()


atexit.register(lambda: scheduler.shutdown())
