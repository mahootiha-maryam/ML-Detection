import pandas as pd
location="measure1.csv"
e=pd.read_csv(location)

location1="measure22.csv"
e1=pd.read_csv(location1)

ids=[]
types=[]

thre1=400000000
thre2=100000000

#for first rule
for sh1,sh2 in enumerate(e['Id']):
   if e.iloc[sh1,4]>=3 and e.iloc[sh1,7]>=thre1 and 0.4<=e.iloc[sh1,10]<=1:
       ids.append(e.iloc[sh1,0])
       types.append("type1")
       
#for second rule
first=[]
second=[]
third=[]
forth=[]
fifth=[]
sixth=[]
shenase=[]
typee=[]
max2=0
max3=0
for l,l1 in enumerate(e1['Id']):
    if e1.iloc[l,7]>max2:
        max2=e1.iloc[l,7]

for i in range(0,max2+1):
    for i1,i2 in enumerate(e1['Id']):
        if e1.iloc[i1,7]==i:
            first.append(e1.iloc[i1,0])
            second.append(e1.iloc[i1,1])

    for i3,i4 in enumerate(first):
        if second[i3] > max3:
            max3=first[i3]
    third.append(max3)
    
    max3=0
    first=[]
    second=[]
    
    
for i8,i9 in enumerate(third):
   if third[i8]!=0:
       forth.append(third[i8])       
       
for i5,i6 in enumerate(e1['Id']):
    for i7,i10 in enumerate(forth):
        if e1.iloc[i5,0]==forth[i7]:
            fifth.append(e1.iloc[i5,4])
            sixth.append(e1.iloc[i5,8])

for i10,i11 in enumerate(forth):
    if (fifth[i10]>=thre2)and (sixth[i10]<=0.6):
        ids.append(forth[i10])
        types.append("type2")       
    
#for third rule
        
for sh3,sh4 in enumerate(e1['Id']):
   if e1.iloc[sh3,5]>=3 and e1.iloc[sh3,3]>=thre2 and 0<=e1.iloc[sh3,2]<0.6:
       ids.append(e1.iloc[sh3,0])
       types.append("type3")

rel=list(zip(ids,types))
pp=pd.DataFrame(data=rel,columns=['id','type'] )
pp.to_csv('method.csv',index=False)      