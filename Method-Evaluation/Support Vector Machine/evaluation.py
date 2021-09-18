import pandas as pd
location="labelofcol.csv"
e=pd.read_csv(location)

location1="labelofcolM.csv"
e1=pd.read_csv(location1)

truepositive=[]
falsengative=[]
falsepositive=[]

precision=0
recall=0
f=0

ids=list(e['ids'])
ids1=list(e1['ids'])
allof=len(ids1)
   
       
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

print(precision)
print(recall)
print(f)

