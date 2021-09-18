import pandas as pd
location="data4.csv"
e=pd.read_csv(location)

import pandas as pd
location1="tag4.csv"
e1=pd.read_csv(location1)


typeofaction=[]
ids=[]
amountofmoney=[]
isfraud=[]
typeoffraud=[]
x=[]

for m,n in enumerate(e1['typeofcrime']):
    if e1.iloc[m,2]=='type2' and e1.iloc[m,1]=='head':
        x.append(e1.iloc[m,0])

for i,l in enumerate(e['typeofaction']):
    if e.iloc[i,6]=='type1':
        typeofaction.append('1')
        ids.append(e.iloc[i,1])
        amountofmoney.append(e.iloc[i,3])
        isfraud.append('1')
        typeoffraud.append('1')
        
        typeofaction.append('1')
        ids.append(e.iloc[i,2])
        amountofmoney.append(e.iloc[i,3])
        isfraud.append('1')
        typeoffraud.append('4')
        
    if e.iloc[i,6]=='type3':
        typeofaction.append('2')
        ids.append(e.iloc[i,2])
        amountofmoney.append(e.iloc[i,3])
        isfraud.append('1')
        typeoffraud.append('3')
        
        typeofaction.append('2')
        ids.append(e.iloc[i,1])
        amountofmoney.append(e.iloc[i,3])
        isfraud.append('1')
        typeoffraud.append('6')
        
     
    if e.iloc[i,6]=='type2':
        if e.iloc[i,1] in x:
            typeofaction.append('2')
            ids.append(e.iloc[i,1])
            amountofmoney.append(e.iloc[i,3])
            isfraud.append('1')
            typeoffraud.append('2')
        else:
        
            typeofaction.append('2')
            ids.append(e.iloc[i,2])
            amountofmoney.append(e.iloc[i,3])
            isfraud.append('1')
            typeoffraud.append('5')
    if e.iloc[i,6]=='none':
        if e.iloc[i,0]=='cash-in':
            typeofaction.append('1')
            ids.append(e.iloc[i,1])
            amountofmoney.append(e.iloc[i,3])
            isfraud.append('0')
            typeoffraud.append('0')
            
            typeofaction.append('1')
            ids.append(e.iloc[i,2])
            amountofmoney.append(e.iloc[i,3])
            isfraud.append('0')
            typeoffraud.append('0')
        if e.iloc[i,0]=='transfer':
            typeofaction.append('2')
            ids.append(e.iloc[i,1])
            amountofmoney.append(e.iloc[i,3])
            isfraud.append('0')
            typeoffraud.append('0')
            
            typeofaction.append('2')
            ids.append(e.iloc[i,2])
            amountofmoney.append(e.iloc[i,3])
            isfraud.append('0')
            typeoffraud.append('0')  
            
        
rel=list(zip(typeofaction,ids,amountofmoney,isfraud,typeoffraud))
pp=pd.DataFrame(data=rel,columns=['typeofaction','ids','amountofmoney','isfraud','typeoffraud'])
pp.to_csv('dataforDL4.csv',index=False)       