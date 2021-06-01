from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
import pickle
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('summary.html')

@app.route('/summary')
def summary():
	return render_template('summary.html')

@app.route('/dashboard')
def dashboard():
	return render_template('dashboard.html')

@app.route('/predict')
def predict():
	return render_template('predictions.html')

@app.route('/model')
def model():
	return render_template('selectedmodel.html')

@app.route('/othermodel')
def othermodel():
	return render_template('othermodels.html')

@app.route('/getpredict',methods=['POST','GET'])
def get_predict():
    if request.method=='POST':
        result=request.form
        X = [[int(result['creditscore']),result['country'], result['gender'],int(result['age']), int(result['tenure']),float(result['balance']), int(result['numproducts']),result['creditcard'],result['activemember'],float(result['estimatedsalary'])]]

    if X[0][7] == 'yes':
        X[0][7]=1
    else:
        X[0][7]=0

    if X[0][8] == 'yes':
        X[0][8]=1
    else:
        X[0][8]=0
    
    X = np.array(X)

    pkl_filename = 'Machine_Learning/Label_Encoder.pkl'
    with open(pkl_filename, 'rb') as file:
        le = pickle.load(file)

    #Load One-Hot encoder: ct
    pkl_filename = 'Machine_Learning/OneHot_Encoder.pkl'
    with open(pkl_filename, 'rb') as file:
        ct = pickle.load(file)
    
    #Load Scaler: sc
    pkl_filename = 'Machine_Learning/Scaler.pkl'
    with open(pkl_filename, 'rb') as file:
        sc = pickle.load(file)

    #Encoding the  Gender column
    X[:,2] = le.transform(X[:,2])

    #Encoding the country column
    X = np.array(ct.transform(X))

    #Scaling all columns
    X = sc.transform(X)

    #Load the ANN model
    ann = load_model("Machine_Learning/customer_churn.h5")

    #Predicting with ANN
    new_pred = ann.predict(X)>0.5 

    if new_pred[0][0] == True:
        result = 'TRUE'
        description = 'The current customer has HIGH probbaility of churning' 
    else:
        result = 'FALSE'
        description = 'The current customer has LOW probbaility of churning'

    return render_template('predictions.html',prediction=result, description=description)

@app.route('/about')
def about():
	return render_template('aboutus.html')

if __name__ == '__main__':
	app.run()