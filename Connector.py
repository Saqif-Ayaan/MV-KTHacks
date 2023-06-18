from flask import Blueprint, render_template, request
import os
import pickle
import pandas as pd

st = Blueprint('start', __name__)
qz = Blueprint('quiz', __name__)
rd = Blueprint('riskDetection', __name__)


@st.route('/')
def home():
    return render_template("Start.html",)

@qz.route('/quiz', methods = ["POST", "GET"])
def assessment():
    if request.method == "POST":
        answers = []
        file = request.files["file"]
        file.save(os.path.join(file.filename))
        f = open(file.filename, 'r')
        if (f.readline().replace("\n", "").replace(" ", "") == 'b'):
            answers.append("CORRECT!")
        else:   
            answers.append("INCORRECT")
        if (f.readline().replace("\n", "").replace(" ", "") == '3'):
            answers.append("CORRECT!")
        else:
            answers.append("INCORRECT")
        if (f.readline().replace("\n", "").replace(" ", "") ==  "T"):
            answers.append("CORRECT!")
        else:
            answers.append("INCORRECT")
        if (f.readline() == 'benign'):
            answers.append("CORRECT!")
        else:
            answers.append("INCORRECT")   
        return render_template("QuizResult.html", Res0 = answers[0], Res1 = answers[1], Res2 = answers[2], Res3 = answers[3])
    return render_template("QuizResult.html")

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

        x = [""]*5
        
        for i in range(len(predictions)):
            if i == (len(predictions) - 1):
                x[i] = (f'patient {i+1} has a tumor in their {substitute.get(predictions[i])}')
            else:
                x[i] = (f'patient {i+1} has a tumor in their {substitute.get(predictions[i])}')
        
        return render_template("Detection.html", pred = x[0], pred2 = x[1], pred3 = x[2], pred4 = x[3], pred5 = x[4])
    return render_template("Detection.html")









