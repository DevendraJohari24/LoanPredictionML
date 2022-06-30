from distutils.log import debug
from flask import Flask, render_template, request,url_for
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

        gen = "Male" if gender==1 else "Female"
        marr =  "Yes" if married == 1 else "No"
        depend = "3+" if dependents ==3 else str(dependents)
        grad = "Yes" if graduate ==0 else "No"
        empl = "Yes" if selfEmployed==1 else "No"
        prop = ""
        if propertyArea == 0:
            prop = "Urban"
        elif propertyArea == 1:
            prop = "SemiUrban"
        else:
            prop = "Rural"
        

    return render_template("submit.html", 
    gender=gen, 
    married=marr,
    dependents=depend, 
    graduate=grad, 
    selfEmployed=empl, 
    applicantIncome=applicantIncome, 
    coApplicantIncome=coApplicantIncome,
    loanAmount=loanAmount,
    loanAmountTerm=loanAmountTerm,
    creditHistory=creditHistory,
    propertyArea=prop,
    loan_pred=loan_pred
    )

if __name__ == "__main__":
    app.run(debug=True)