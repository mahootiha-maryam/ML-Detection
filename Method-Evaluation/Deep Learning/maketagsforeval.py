
import pandas as pd
location="dataforDL1.csv"
e=pd.read_csv(location)
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

location="dataforDl1.csv"
e=pd.read_csv(location)

location1="lm.csv"
e1=pd.read_csv(location1)

x=list(e['ids'])
y=list(e1['label'])

rel=list(zip(x,y))
pp=pd.DataFrame(data=rel,columns=['ids','tags'])
pp.to_csv('labelofmethod.csv',index=False)


location="labelofmethod.csv"
e=pd.read_csv(location)

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

