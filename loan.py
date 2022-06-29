import  numpy as np
import  pandas as pd
from sklearn.linear_model import LogisticRegression


def loan_prediction(dependents, graduate, applicantIncome, coApplicantIncome, loanAmount, creditHistory, propertyArea,  gender, married, selfEmployed):
    train = pd.read_csv('dataset/train.csv')
    # Gender Column
    train['Gender'] = train['Gender'].replace(np.nan ,train['Gender'].mode()[0])
    # Married Column
    train['Married'] = train['Married'].replace(np.nan, train['Married'].mode()[0])
    # Dependent Column
    train['Dependents'] = train['Dependents'].fillna("0")
    # Self Employed Column
    train['Self_Employed'] = train['Self_Employed'].replace(np.nan, train['Self_Employed'].mode()[0])
    # Credit History Column
    train['Credit_History'] = train['Credit_History'].replace(np.nan,train['Credit_History'].mode()[0])
    # Load Amount 
    train['LoanAmount'] = train['LoanAmount'].fillna(train['LoanAmount'].mean()).astype(int)
    #drop Loan Amount Term
    train.drop(['Loan_Amount_Term'], axis = 1 , inplace =True)

    # Categorical to Numerical Conversion
    dummies = pd.get_dummies(train.Gender, prefix = 'Gender', drop_first = True)
    # Concatenate the dummies to original dataframe
    train = pd.concat([train, dummies], axis='columns')
    # drop the values
    train.drop(['Gender'], axis='columns', inplace=True)

    values = {'0':'0', '1':'1', '2':'2', '3+':'3'}

    train['Dependents'] = train['Dependents'].replace(values).astype(int)

    # get the dummies and store it in a variable
    dummies = pd.get_dummies(train.Married, prefix = 'Married', drop_first = True)
    # Concatenate the dummies to original dataframe
    train = pd.concat([train, dummies], axis='columns')
    # drop the values
    train.drop(['Married'], axis='columns', inplace=True)


    # get the dummies and store it in a variable
    dummies = pd.get_dummies(train.Self_Employed, prefix = 'Self_Employed', drop_first = True)
    # Concatenate the dummies to original dataframe
    train = pd.concat([train, dummies], axis='columns')
    # drop the values
    train.drop(['Self_Employed'], axis='columns', inplace=True)

    train['Education'] = train['Education'].map( {'Graduate': 0, 'Not Graduate': 1} ).astype(int)

    train['Property_Area'] = train['Property_Area'].map( {'Urban': 0, 'Semiurban': 1 ,'Rural': 2  } ).astype(int)

    train['Loan_Status'] = train['Loan_Status'].map( {'N': 0, 'Y': 1 } ).astype(int)

    train.drop(['Loan_ID'], axis = 1 , inplace =True)

    X = train.drop('Loan_Status' , axis = 1)
    y = train['Loan_Status']

    model = LogisticRegression()
    model.fit(X , y)
    data = [[int(dependents), int(graduate), int(applicantIncome), float(coApplicantIncome), float(loanAmount), float(creditHistory), int(propertyArea),  int(gender), int(married), int(selfEmployed)]]
    df = pd.DataFrame(data, columns=['Dependents', 'Education', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Credit_History', 'Property_Area', 'Gender_Male', 'Married_Yes', 'Self_Employed_Yes'])
    
    pred_data = model.predict(df)
    print(pred_data)
    results = { 0: 'Not Applicable', 1: 'Applicable'}
    return  results[pred_data[0]]
   