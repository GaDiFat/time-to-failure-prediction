import numpy as np
import pandas as pd

for i in [1,2,3,4]:
    
    df=pd.read_csv("Test_"+str(i)+".csv")
    RUL=list()
    for id in np.unique(df['ID']):
        max_RUL=max(df[df['ID']==id]['Cycle'])
        RUL_id=[max_RUL-x for x in df[df['ID']==id]['Cycle'].to_list()]
        RUL=RUL+RUL_id
    df['RUL']=RUL
    
    df.to_csv("Test_"+str(i)+".csv", index=False)
    
    df=pd.read_csv("Train_"+str(i)+".csv")
    RUL=list()
    for id in np.unique(df['ID']):
        max_RUL=max(df[df['ID']==id]['Cycle'])
        RUL_id=[max_RUL-x for x in df[df['ID']==id]['Cycle'].to_list()]
        RUL=RUL+RUL_id
    df['RUL']=RUL
    df.to_csv("Train_"+str(i)+".csv", index=False)