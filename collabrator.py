import pandas as pd
location="measure22.csv"
e=pd.read_csv(location)

location1="method.csv"
e1=pd.read_csv(location1)

location2="measure11.csv"
e2=pd.read_csv(location2)

first=[]
second=[]
third=[]
forth=[]

headid1=e1['id']
hid1=[]
typeofc1=e1['type']
typeofc2=[]
first1=[]

extraid1=e2['Id']
moduleof1=e2['modularity_class']
lx1=len(extraid1)

for s1 in range(0,len(headid1)):
    if typeofc1[s1]=="type1":
        hid1.append(headid1[s1])
        typeofc2.append(typeofc1[s1])

lh1=len(hid1)

for i1 in range(0,lh1):
    for l1 in range(0,lx1):
        if hid1[i1]==extraid1[l1]:
            first1.append(moduleof1[l1])
            
for j1 in range(0,lh1):
    for c1 in range(0,lx1):
        if hid1[j1]!=extraid1[c1] and moduleof1[c1]==first1[j1]:
            second.append(extraid1[c1])
            third.append(typeofc2[j1])
            forth.append(hid1[j1])
                
headid=e1['id']
hid=[]
typeofc=e1['type']
typeofc1=[]

extraid=e['Id']
moduleof=e['modularity_class']
lx=len(extraid)

for s in range(0,len(headid)):
    if typeofc[s]!="type1":
        hid.append(headid[s])
        typeofc1.append(typeofc[s])
        
lh=len(hid)

for i in range(0,lh):
    for l in range(0,lx):
        if hid[i]==extraid[l]:
            first.append(moduleof[l])
            
for j in range(0,lh):
    for c in range(0,lx):
        if hid[j]!=extraid[c] and moduleof[c]==first[j]:
            second.append(extraid[c])
            third.append(typeofc1[j])
            forth.append(hid[j])




    
rel=list(zip(second,third,forth))
pp=pd.DataFrame(data=rel,columns=['collabratorid','type','headid'])
pp.to_csv('collaborator.csv',index=False)


