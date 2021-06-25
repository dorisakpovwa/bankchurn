# bankchurn
Project Name: TEAM GREEDY  BANKERS

Project Team:

DORIS AKPOVWA

NADER SALAMEH

CARLOS PAZOS


PROJECT SUMMARY

We are a European bank with operations in France, Germany, and Spain. Our bank is focused on ensuring we retain our customers globally and have embarked on a machine learning project using historical data to evaluate our customer behavior since they started banking with us. 

The goal of the project is to predict the bank customers that are likely going to churn or stop using our services. This will enable us to be proactive in providing services and products tailored to the project outcome that will ultimately increase our market share. 


PROJECT DESCRIPTION 

The aim is to predict bank customers that will churn and those that will not. We performed exploratory data analysis with visualizations in Tableau using attributes such as Age, Sex, Country, number of bank products they used, their credit card history, estimated salaries and bank balances. This enabled us to identify certain groups of customers that had a high potential to churn.  Subsequently we used machine learning algorithm to predict customer churn.

APPROACH

We tested out the accuracy of five different Machine Learning Classification Models ( K-Nearest Neigbour, Support Vector Machine, Decision Tree, Random Forest and Neural Networks). We went further to validate our models using (Confusion Matrix, F1 score, Accuracy, Feature Importance, Error curves, Random forest decision trees and ANN architecture).

Upon careful study of the various models and validations. We decided to go with the ANN because we had a relatively higher F1 score and hence a higher confidence on the prediction also this will give the bank scalability as the get more customers.

Deployment:
The app was deployed in Heroku:
https://gtbankchurn.herokuapp.com/summary

Bank Data Source

Historical data was taken from the Kaggle website that included information of banks in Europe including demographic information, services. The size of the dataset is 10,000 records.

URL: https://www.kaggle.com/adammaus/predicting-churn-for-bank-customers

