# -*- coding: utf-8 -*-
"""
Created on Thu May 24 11:08:21 2018

@author: srikanth.soma
"""

from flask import Flask, request,jsonify
import pandas as pd
import pickle
import sys
import json
from datetime import datetime, date
app = Flask(__name__)
 
@app.route("/fetch_roi", methods =['Get'])
def hello():
    
    #test = pd.read_json("https://api.rubique.com/v3/sample", orient = 'records')
    #return test
    finbank_classification  = request.args.get('finbank_classification')
    sanctioned_loan_amount = request.args.get('sanctioned_loan_amount')
    disbursed_tenure = request.args.get('disbursed_tenure')
    gross_monthly_income = request.args.get('gross_monthly_income')
    current_city = request.args.get('current_city')
    disbursal_date = request.args.get('disbursal_date')
    dob = request.args.get('dob')
    residence_year = request.args.get('residence_year')
    total_working_experience = request.args.get('total_working_experience')
    current_company_experience = float(request.args.get('current_company_experience'))
    if finbank_classification == None:
        status=400
        message = 'missing data'
        ROI = "Please provide finbank name to view interest rates"
        predicts = pd.DataFrame({'ROI':ROI,'message':message,'status':status}, index=[0])
        responses = predicts.to_json(orient="records",lines=True)
        return (responses)
        sys.exit()
    elif sanctioned_loan_amount == None:
        status=400
        message = 'missing data'
        ROI = "Please provide loan amount to view interest rates"
        predicts = pd.DataFrame({'ROI':ROI,'message':message,'status':status}, index=[0])
        responses = predicts.to_json(orient="records",lines=True)
        return (responses)
        sys.exit()
    elif disbursed_tenure == None:
        status=400
        message = 'missing data'
        ROI = "Please provide tenure to view interest rates"
        predicts = pd.DataFrame({'ROI':ROI,'message':message,'status':status}, index=[0])
        responses = predicts.to_json(orient="records",lines=True)
        return (responses)
        sys.exit()
    elif gross_monthly_income == None:
        status=400
        message = 'missing data'
        ROI = "Please provide gross monthly income to view interest rates"
        predicts = pd.DataFrame({'ROI':ROI,'message':message,'status':status}, index=[0])
        responses = predicts.to_json(orient="records",lines=True)
        return (responses)
        sys.exit()
    elif current_city == None:
        status=400
        message = 'missing data'
        ROI = "Please provide current city you are residing in to view interest rates"
        predicts = pd.DataFrame({'ROI':ROI,'message':message,'status':status}, index=[0])
        responses = predicts.to_json(orient="records",lines=True)
        return (responses)
        sys.exit()
    elif disbursal_date == None:
        status=400
        message = 'missing data'
        ROI = "Please provide disbursal_date to view interest rates"
        predicts = pd.DataFrame({'ROI':ROI,'message':message,'status':status}, index=[0])
        responses = predicts.to_json(orient="records",lines=True)
        return (responses)
        sys.exit()
    elif dob == None:
        status=400
        message = 'missing data'
        ROI = "Please provide date of birth to view interest rates"
        predicts = pd.DataFrame({'ROI':ROI,'message':message,'status':status}, index=[0])
        responses = predicts.to_json(orient="records",lines=True)
        return (responses)
        sys.exit()
    elif residence_year == None:
        status=400
        message = 'missing data'
        ROI = "Please provide number of years you are staying at your current loaction to view interest rates"
        predicts = pd.DataFrame({'ROI':ROI,'message':message,'status':status}, index=[0])
        responses = predicts.to_json(orient="records",lines=True)
        return (responses)
        sys.exit()
    elif total_working_experience == None:
        status=400
        message = 'missing data'
        ROI = "Please provide total working experience to view interest rates"
        predicts = pd.DataFrame({'ROI':ROI,'message':message,'status':status}, index=[0])
        responses = predicts.to_json(orient="records",lines=True)
        return (responses)
        sys.exit()
    elif current_company_experience == None:
        status=400
        message = 'missing data'
        ROI = "Please provide current company experience to view interest rates"
        predicts = pd.DataFrame({'ROI':ROI,'message':message,'status':status}, index=[0])
        responses = predicts.to_json(orient="records",lines=True)
        return (responses)
        sys.exit()
    
    else:    
        finbank_classification = int(finbank_classification)
        sanctioned_loan_amount = int(sanctioned_loan_amount)
        disbursed_tenure = int(disbursed_tenure)
        gross_monthly_income = int(gross_monthly_income)
        residence_year = int(residence_year)
        total_working_experience = int(total_working_experience)
        current_company_experience = float(current_company_experience)
        #age calculation
        born = datetime.strptime(dob,"%Y-%m-%d")
        today = date.today()
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        age = float(age) 
    
        month= datetime.strptime(disbursal_date,"%Y-%m-%d").month
        current_city_mapping = {'Ahmedabad': 0,
 'Bangalore': 1,
 'Bhubaneswar': 2,
 'Chennai': 3,
 'Delhi': 4,
 'Durgapur': 5,
 'Ghaziabad': 6,
 'Gurgaon': 7,
 'Hyderabad': 8,
 'Jaipur': 9,
 'Kolkata': 10,
 'Mumbai': 11,
 'Noida': 12,
 'Pune': 13,
 'Thane': 14,
 'Vadodara': 15,
 'Vizag': 16}
    
        test_data = pd.DataFrame({'sanctioned_loan_amount': sanctioned_loan_amount, 
                              'finbank_classification': finbank_classification,
                              'disbursed_tenure': disbursed_tenure,
                              'current_city': current_city,
                              'age': age,
                              'residence_year': residence_year,
                              'gross_monthly_income': gross_monthly_income,
                              'current_company_experience' : current_company_experience,
                              'total_working_experience': total_working_experience,
                              'month': month,}, 
                              columns=['sanctioned_loan_amount', 'finbank_classification', 'disbursed_tenure',
                                       'current_city', 'age','residence_year',
                                       'gross_monthly_income','current_company_experience',
                                       'total_working_experience','month'], index=[0])
        test_data = test_data.replace({"current_city":current_city_mapping})
        tunedmodel_final = 'tunedmodel_final.sav'
        loaded_model = pickle.load(open(tunedmodel_final, 'rb'))
    
        prediction = loaded_model.predict(test_data)
    
        prediction_final = prediction[0]
        prediction_final = round(prediction_final,2)
        predicts = list(pd.Series(prediction_final))
        #predicts = pd.DataFrame({'Rate_of_interest':predicts})
    
        #print(prediction_final)
    
        #responses = jsonify(predictions = predicts.to_json(orient="records"))
        #responses.status_code = 200
        if prediction_final is not None:
                status = 200
                message = "ok"
        predicts = pd.DataFrame({'ROI':predicts,'message':message,'status':status})
    
        print(prediction_final)
    
        responses = predicts.to_json(orient="records",lines=True)
    
        return (responses)
    
 
if __name__ == "__main__":
    app.run()