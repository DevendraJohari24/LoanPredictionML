from distutils.log import debug
from flask import Flask, render_template, request
import loan as l

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/submit", methods=['POST'])
def submit():
    if request.method == "POST":
        gender = request.form['gender']
        dependents = request.form['dependents']
        graduate = request.form['graduate']
        selfEmployed = request.form['employed']
        applicantIncome = request.form['applicantIncome']
        coApplicantIncome = request.form['coApplicantIncome']
        loanAmount = request.form['loanAmount']
        loanAmountTerm = request.form['loanAmountTerm']
        creditHistory = request.form['creditHistory']
        propertyArea = request.form['propertyArea']
        married = request.form['married']

        loan_pred = l.loan_prediction(dependents, graduate, applicantIncome, coApplicantIncome, loanAmount, creditHistory, propertyArea,  gender, married, selfEmployed)


    return render_template("submit.html", 
    gender=gender, 
    dependents=dependents, 
    graduate=graduate, 
    selfEmployed=selfEmployed, 
    applicantIncome=applicantIncome, 
    coApplicantIncome=coApplicantIncome,
    loanAmount=loanAmount,
    loanAmountTerm=loanAmountTerm,
    creditHistory=creditHistory,
    propertyArea=propertyArea,
    loan_pred=loan_pred
    )

if __name__ == "__main__":
    app.run(debug=True)