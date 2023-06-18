from flask import Blueprint, render_template, request
import os
import pickle
import pandas as pd

st = Blueprint('start', __name__)
rd = Blueprint('riskDetection', __name__)


@st.route('/')
def home():
    return render_template("Start.html",)

@st.route('/', methods = ["POST", "GET"])
def assessment():
    if request.method == "POST":
        answers = []
        ans1 = request.form['ans1']
        ans2 = request.form['ans2']
        ans3 = request.form['ans3']
        ans4 = request.form['ans4']
        if (ans1 == 'b'):
            answers.append("CORRECT!")
        else:   
            answers.append("INCORRECT!")
        if (ans2 == '3'):
            answers.append("CORRECT!")
        else:
            answers.append("INCORRECT!")
        if (ans3 == "T"):
            answers.append("CORRECT!")
        else:
            answers.append("INCORRECT!")
        if (ans4 == 'benign'):
            answers.append("CORRECT!")
        else:
            answers.append("INCORRECT!")   
        return render_template("Start.html", Res0 = answers[0], Res1 = answers[1], Res2 = answers[2], Res3 = answers[3])
    return render_template("Start.html")

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

        x = [""] * 5
        
        for i in range(len(predictions)):
            if i == (len(predictions) - 1):
                x[i] = (f"patient {i+1}'s origin of tumor is their {substitute.get(predictions[i])}")
            else:
                x[i] = (f"patient {i+1}'s origin of tumor is their {substitute.get(predictions[i])}")
        
        return render_template("Detection.html", pred = x[0], pred2 = x[1], pred3 = x[2], pred4 = x[3], pred5 = x[4])
    return render_template("Detection.html")









