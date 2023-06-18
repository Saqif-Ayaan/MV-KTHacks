from flask import Blueprint, render_template, request
import os
import pickle
import pandas as pd

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
        file.save(os.path.join(file.filename))
        
        tumor_data = pd.read_csv(file.filename)
        model = pickle.load(open("tumormodel_svm_3.pickle", "rb"))
        
        predictions = model.predict(tumor_data.values)

        substitute = {
            1: "lung",
            2: "head and neck",
            3: "esophagus",
            4: "thyroid",
            5: "stomach",
            6: "duoden and small intestine",
            7: "colon",
            8: "rectum",
            9: "anus",
            10: "salivary glands",
            11: "pancreas",
            12: "gallblader",
            13: "liver",
            14: "kidney",
            15: "bladder",
            16: "testis",
            17: "prostate",
            18: "ovary",
            19: "corpus uteri",
            20: "cervix uteri",
            21: "vagina",
            22: "breast"
        }

        x = ""
        
        for i in range(len(predictions)):
            if i == (len(predictions) - 1):
                x += (f'patient {i+1} has a tumor in their {substitute.get(predictions[i])}')
            else:
                x += (f'patient {i+1} has a tumor in their {substitute.get(predictions[i])} / ')
        
        return render_template("Detection.html", pred = x)
    return render_template("Detection.html")








