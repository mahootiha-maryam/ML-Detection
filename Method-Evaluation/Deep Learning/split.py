# -*- coding: utf-8 -*-
"""
Created on Sun May 31 20:59:01 2020

@author: Asus
"""

import pandas as pd
location="dataforDl1.csv"
e=pd.read_csv(location)


location1="tagofmethod.csv"
e1=pd.read_csv(location1)

x=[]
tags=[]
tags1=[]
for i,l in enumerate(e['typeoffraud']):
    if e.iloc[i,4]== 4:
        x.append(i)
    if e.iloc[i,4]==5:
        x.append(i)
    if e.iloc[i,4]==6:
        x.append(i)
for i1,l1 in enumerate(e1['label']):
    for i2,l2 in enumerate(x):
        if i1==i2:
            tags.append(e1.iloc[i2,0])
        else:
            tags1.append(e1.iloc[i2,0])
rel=list(zip(tags))
pp=pd.DataFrame(data=rel,columns=['tags'])
pp.to_csv('labelofcol.csv',index=False)

rel=list(zip(tags1))
pp=pd.DataFrame(data=rel,columns=['tags'])
pp.to_csv('labelofhead.csv',index=False)