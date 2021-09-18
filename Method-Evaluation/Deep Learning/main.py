import keras
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
import matplotlib.pyplot as plt
import time
start_time=time.time()
location="dataforDl.csv"
data=pd.read_csv(location)
data_columns=data.columns
xtrain = data[data_columns[data_columns != 'typeoffraud']] 
ytrain=data['typeoffraud']


location1="dataforDl1.csv"
data1=pd.read_csv(location1)
data1_columns=data1.columns
xtest = data1[data1_columns[data1_columns != 'typeoffraud']] 
ytest=data1['typeoffraud']

xtrain_norm = (xtrain - xtrain.mean()) / xtrain.std()
xtest_norm = (xtest - xtest.mean()) / xtest.std()
n_cols = xtrain_norm.shape[1]

ytrain=to_categorical(ytrain)
ytest=to_categorical(ytest)

num_classes=ytrain.shape[1]
print(num_classes)

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
print('---%s seconds---'%(time.time()-start_time))