import numpy as np
import pandas as pd

import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

df_train = pd.read_csv('train.csv')

train=pd.DataFrame(df_train)
train = pd.crosstab(index=train["Type"],columns="count")

type = [[1,"Dog"], [2,"Cat"]]
pet = pd.DataFrame(type, columns = ['Type','Animal'])

results = train.merge(pet,on='Type')

r1 = results[['Animal','count']]

print("")
print("Data from train.csv")
print(train)
print("-------------------")
print("Self-created type key")
print(pet)
print("-------------------")
print('combined data:')
print(r1)
#print("")


