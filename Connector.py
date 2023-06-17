from flask import Blueprint, render_template, request
import os

st = Blueprint('start', __name__)
qz = Blueprint('quiz', __name__)
rd = Blueprint('riskDetection', __name__)


@st.route('/')
def home():
    return render_template("Start.html")

@qz.route('/quiz')
def assessment():
    return render_template("Quiz.html")

@rd.route('/riskDetection', methods = ["POST", "GET"])
def det():
    if request.method == "POST":
        file = request.files["file"]
        file.save(os.path.join("Data", file.filename))
    return render_template("Detection.html")








