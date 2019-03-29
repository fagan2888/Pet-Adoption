import numpy as np
import pandas as pd

import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

df_train = pd.read_csv('train.csv')
df_state = pd.read_csv('state_labels.csv')

train=pd.DataFrame(df_train)
train = pd.crosstab(index=train["State"],columns="count")
train.index.name = 'StateID'

state=pd.DataFrame(df_state)

results = train.merge(state,on='StateID')

r1 = results[['StateName','count']]

print("")
print("Data from train.csv")
print(train)
print("-------------------")
print("Data from state_labels.csv")
print(state)
print("-------------------")
print('combined data:')
print(r1)
print("")
print("Note:The state of Perlis (no. 41380) has zero entries")


