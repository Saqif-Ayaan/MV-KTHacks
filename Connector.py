from flask import Blueprint, render_template

connector = Blueprint('connector', __name__)

@connector.route('/')
def home():
    return render_template("Start.html")