import pandas as pd 
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
import time
import multiprocessing as mp
start_time=time.time()

def svm(location1,location2):

    data=pd.read_csv(location1)
    data_columns=data.columns
    xtrain = data[data_columns[data_columns != 'typeoffraud']] 
    ytrain=data['typeoffraud']
    
    data1=pd.read_csv(location2)
    data1_columns=data1.columns
    xtest = data1[data1_columns[data1_columns != 'typeoffraud']] 

    
    from sklearn import svm
    clf=svm.SVC(kernel='rbf')
    clf.fit(xtrain,ytrain)
    
    ypredict=clf.predict(xtest)
    rel=list(zip(ypredict))
    pp=pd.DataFrame(data=rel,columns=['label'])
    pp.to_csv('label.csv',index=False)
###########################################################################################################
def maketags(location2,location3):

    e=pd.read_csv(location2)
    tags=[]
    ids=[]
    tags1=[]
    ids1=[]
    for i,l in enumerate(e['typeoffraud']):
        if l==1 or l==2 or l==3:
          ids.append(e.iloc[i,1])
          tags.append(e.iloc[i,4])
        if l==4 or l==5 or l==6:
          ids1.append(e.iloc[i,1])
          tags1.append(e.iloc[i,4])
          
    rel=list(zip(ids,tags))
    pp=pd.DataFrame(data=rel,columns=['ids','tags'])
    pp.to_csv('labelofhead.csv',index=False)
    
    rel1=list(zip(ids1,tags1))
    pp1=pd.DataFrame(data=rel1,columns=['ids','tags'])
    pp1.to_csv('labelofcol.csv',index=False)
    
    
    e1=pd.read_csv(location3)
    
    x=list(e['ids'])
    y=list(e1['label'])

    
    rel=list(zip(x,y))
    pp=pd.DataFrame(data=rel,columns=['ids','tags'])
    pp.to_csv('labelofmethod.csv',index=False)
    
    locationnew="labelofmethod.csv"
    e=pd.read_csv(locationnew)
    
    idof=[]
    tag=[]
    idof1=[]
    tag1=[]
    for i,l in enumerate(e['tags']):
        if l==1 or l==2 or l==3:
          idof.append(e.iloc[i,0])
          tag.append(e.iloc[i,1])
        if l==4 or l==5 or l==6:
          idof1.append(e.iloc[i,0])
          tag1.append(e.iloc[i,1])
          
    rel=list(zip(idof,tag))
    pp=pd.DataFrame(data=rel,columns=['ids','tags'])
    pp.to_csv('labelofheadM.csv',index=False)
    
    rel1=list(zip(idof1,tag1))
    pp1=pd.DataFrame(data=rel1,columns=['ids','tags'])
    pp1.to_csv('labelofcolM.csv',index=False)
#############################################################################################################
def evalofhead(location4,location5):
    e=pd.read_csv(location4)
    e1=pd.read_csv(location5)
    
    truepositive=[]
    falsengative=[]
    falsepositive=[]
    
    precision=0
    recall=0
    f=0
    
    ids=list(e['ids'])
    ids1=list(e1['ids'])
 
    for item in ids:
        if item in ids1:
            truepositive.append(item)
        else:
            falsengative.append(item)
            
    for item1 in ids1:
        if item1 in ids:
            pass
        else:
            falsepositive.append(item1)
    
    tp=len(truepositive)
    fn=len(falsengative)
    fp=len(falsepositive)
    
    precision=(tp/(tp+fp))
    recall=(tp/(tp+fn))
    f=2*((precision*recall)/(precision+recall))
    
    print("%s :precision for head detection"%precision)
    print("%s :recall for head detection"%recall)
    print("%s :f-measure for head detection"%f)
#################################################################################################################
def evalofcol(location6,location7):
    e=pd.read_csv(location6)
    e1=pd.read_csv(location7)
    
    truepositive=[]
    falsengative=[]
    falsepositive=[]
    
    precision=0
    recall=0
    f=0
    
    ids=list(e['ids'])
    ids1=list(e1['ids'])

    for item in ids:
        if item in ids1:
            truepositive.append(item)
        else:
            falsengative.append(item)
            
    for item1 in ids1:
        if item1 in ids:
            pass
        else:
            falsepositive.append(item1)
    
    tp=len(truepositive)
    fn=len(falsengative)
    fp=len(falsepositive)
    
    precision=(tp/(tp+fp))
    recall=(tp/(tp+fn))
    f=2*((precision*recall)/(precision+recall))
    
    print("%s :precision for colleague detection"%precision)
    print("%s :recall for colleague detection"%recall)
    print("%s :f-measure for colleague detection"%f)

# print('precision',metrics.recall_score(ytest,ypredict))

# LR=LogisticRegression(random_state=0,solver='lbfgs',multi_class='ovr').fit(xtrain,ytrain)
# labelofreg=LR.predict(xtest)

# MN=MPLClassifier(solver='lbfgs',alpha=1e-5,hidden_layer_size=(1,50,10),random_state=1).fit(xtrain,ytrain)
# NN=MN.predict(xtest)
#######################################################################################################################    
location1="dataforDl.csv"
location2="dataforDl2.csv"
location3="label.csv"
location4="labelofhead.csv"
location5="labelofheadM.csv"
location6="labelofcol.csv"
location7="labelofcolM.csv"

p1= mp.Process(target=svm, args=(location1,location2))
p1.start()
p1.join()

p2= mp.Process(target=maketags, args=(location2,location3))
p2.start()
p2.join()

evalofhead(location4,location5)
evalofcol(location6,location7)
print('---%s seconds---'%(time.time()-start_time))