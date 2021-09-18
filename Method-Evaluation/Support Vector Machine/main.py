import pandas as pd 
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
def svm(location1,location2):

    data=pd.read_csv(location1)
    data_columns=data.columns
    xtrain = data[data_columns[data_columns != 'typeoffraud']] 
    ytrain=data['typeoffraud']
    
    data1=pd.read_csv(location2)
    data1_columns=data1.columns
    xtest = data1[data1_columns[data1_columns != 'typeoffraud']] 
    ytest=data1['typeoffraud']
    
    from sklearn import svm
    clf=svm.SVC(kernel='rbf')
    clf.fit(xtrain,ytrain)
    
    ypredict=clf.predict(xtest)
    rel=list(zip(ypredict))
    pp=pd.DataFrame(data=rel,columns=['label'])
    pp.to_csv('label.csv',index=False)
# print('precision',metrics.recall_score(ytest,ypredict))

# LR=LogisticRegression(random_state=0,solver='lbfgs',multi_class='ovr').fit(xtrain,ytrain)
# labelofreg=LR.predict(xtest)

# MN=MPLClassifier(solver='lbfgs',alpha=1e-5,hidden_layer_size=(1,50,10),random_state=1).fit(xtrain,ytrain)
# NN=MN.predict(xtest)
    
location1="dataforDl1.csv"
location2="dataforDl.csv"
svm(location1,location2)