import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
import time
import multiprocessing as mp
start_time=time.time()
def deepl(location1,location2):

    data=pd.read_csv(location1)
    data_columns=data.columns
    xtrain = data[data_columns[data_columns != 'typeoffraud']] 
    ytrain=data['typeoffraud']
    
    
    
    data1=pd.read_csv(location2)
    data1_columns=data1.columns
    xtest = data1[data1_columns[data1_columns != 'typeoffraud']] 
    ytest=data1['typeoffraud']
    
    xtrain_norm = (xtrain - xtrain.mean()) / xtrain.std()
    xtest_norm = (xtest - xtest.mean()) / xtest.std()
    n_cols = xtrain_norm.shape[1]
    
    ytrain=to_categorical(ytrain)
    ytest=to_categorical(ytest)
    
    num_classes=ytrain.shape[1]
    
    def classification_model():
        # create model
        model = Sequential()
        model.add(Dense(100,activation='relu', input_shape=(n_cols,)))
        model.add(Dense(100, activation='relu'))
        model.add(Dense(num_classes, activation='softmax'))
        
        
        # compile model
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        return model
    # build the model
        
    model = classification_model()
    
    # fit the model
    model.fit(xtrain_norm, ytrain, validation_data=(xtest_norm, ytest), epochs=10, verbose=1)
    
    # evaluate the model
    # test_loss,test_acc=model.evaluate(xtest_norm, ytest)
    test_labels_p=model.predict(xtest_norm)
    test_labels_p=np.argmax(test_labels_p,axis=1)
    rel=list(zip(test_labels_p))
    pp=pd.DataFrame(data=rel,columns=['label'])
    pp.to_csv('label.csv',index=False)
################################################################################################################
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
########################################################################################################
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
############################################################################################################
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
############################################################################################################   
location1="dataforDl.csv"
location2="dataforDl1.csv"
location3='label.csv'
location4="labelofhead.csv"
location5="labelofheadM.csv"
location6="labelofcol.csv"
location7="labelofcolM.csv"

p1= mp.Process(target=deepl, args=(location1,location2))
p1.start()
p1.join()

p2= mp.Process(target=maketags, args=(location2,location3))
p2.start()
p2.join()

evalofhead(location4,location5)
evalofcol(location6,location7)

print('---%s seconds---'%(time.time()-start_time))