import pandas as pd
location="Mll.csv"
e=pd.read_csv(location)

e1= e.drop(e[(e.typeofaction!="cash-in")].index)
e1.to_csv('1.csv',index=False)

e2= e.drop(e[(e.typeofaction!="transfer")].index)
e2.to_csv('2.csv',index=False)

location1="1.csv"
location2="2.csv"

e3=pd.read_csv(location1)
e4=pd.read_csv(location2)

rel1=list(zip(e3.sourceid,e3.destinationid,e3.amountofmoney))
pp1=pd.DataFrame(data=rel1 , columns=['source','target','weight'])
pp1.to_csv('gephicsv1.csv',index=False)

rel2=list(zip(e4.sourceid,e4.destinationid,e4.amountofmoney))
pp2=pd.DataFrame(data=rel2 , columns=['source','target','weight'])
pp2.to_csv('gephicsv2.csv',index=False)