# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 12:51:18 2020

@author: Asus
"""
import pandas as pd 
from sklearn.metrics import confusion_matrix 
from sklearn.tree import DecisionTreeClassifier 
from sklearn.metrics import accuracy_score 
from sklearn.metrics import classification_report 
import time
start_time=time.time()

def train_using_gini(xtrain, xtest, ytrain): 
  
    # Creating the classifier object 
    clf_gini = DecisionTreeClassifier(criterion = "gini", 
            random_state = 100,max_depth=3, min_samples_leaf=5) 
  
    # Performing training 
    clf_gini.fit(xtrain, ytrain) 
    return clf_gini 

def tarin_using_entropy(xtrain, xtest, ytrain): 
  
    # Decision tree with entropy 
    clf_entropy = DecisionTreeClassifier( 
            criterion = "entropy", random_state = 100, 
            max_depth = 3, min_samples_leaf = 5) 
  
    # Performing training 
    clf_entropy.fit(xtrain, ytrain) 
    return clf_entropy 

def prediction(xtest, clf_object): 
  
    # Predicton on test with giniIndex 
    y_pred = clf_object.predict(xtest) 
    print("Predicted values:") 
    print(y_pred) 
    return y_pred 

def cal_accuracy(ytest, y_pred): 
      
    print("Confusion Matrix: ", 
        confusion_matrix(ytest, y_pred)) 
      
    print ("Accuracy : ", 
    accuracy_score(ytest,y_pred)*100) 
      
    print("Report : ", 
    classification_report(ytest, y_pred)) 

location="dataforDl1.csv"
data=pd.read_csv(location)
data_columns=data.columns
xtrain = data[data_columns[data_columns != 'typeoffraud']] 
ytrain=data['typeoffraud']


location1="dataforDl.csv"
data1=pd.read_csv(location1)
data1_columns=data1.columns
xtest = data1[data1_columns[data1_columns != 'typeoffraud']] 
ytest=data1['typeoffraud']

clf_gini = train_using_gini(xtrain, xtest, ytrain) 
clf_entropy = tarin_using_entropy(xtrain, xtest, ytrain) 
y_pred_gini = prediction(xtest, clf_gini) 
#cal_accuracy(ytest, y_pred_gini) 
y_pred_entropy = prediction(xtest, clf_entropy) 
#cal_accuracy(ytest, y_pred_entropy) 