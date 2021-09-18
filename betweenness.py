import pandas as pd
location="shakhes2.csv"
e=pd.read_csv(location)

max1=0
betweenness=[]

for i,i1 in enumerate(e['Id']):
    if e.iloc[i,12]>max1:
        max1=e.iloc[i,12]

for i2,i3 in enumerate(e['Id']):
    betweenness.append(e.iloc[i2,12]/max1)
    


rel=list(zip(e['Id'],e['Eccentricity'],e['closnesscentrality'],e['weighted indegree'],e['weighted outdegree'],e['indegree'],e['outdegree'],e['modularity_class'],betweenness))
pp=pd.DataFrame(data=rel,columns=['Id','Eccentricity','closnesscentrality','weighted indegree','weighted outdegree','indegree','outdegree','modularity_class','betweennesscentrality'])
pp.to_csv('measure22.csv',index=False)