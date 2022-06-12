from flask import render_template
from flask import Request
from app import FlaskApp


@FlaskApp.route("/")
def homeIndex():

