import numpy as np
import pandas as pd

import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

df_train = pd.read_csv('train.csv')

df=pd.DataFrame(df_train)

m1 = pd.crosstab(index=df_train["Type"],columns="count")
m2 = pd.crosstab(index=df_train["Gender"],columns="count")
m3 = pd.crosstab(index=df_train["Color1"],columns="count")
m33 = pd.crosstab(index=df_train["Color2"],columns="count")
m4 = pd.crosstab(index=df_train["MaturitySize"],columns="count")
m5 = pd.crosstab(index=df_train["FurLength"],columns="count")
m6 = pd.crosstab(index=df_train["Vaccinated"],columns="count")
m7 = pd.crosstab(index=df_train["State"],columns="count")
m8 = pd.crosstab(index=df_train["VideoAmt"],columns="count")
m9 = pd.crosstab(index=df_train["PhotoAmt"],columns="count")
m10 = pd.crosstab(index=df_train["AdoptionSpeed"],columns="count")
m11 = pd.crosstab(index=df_train["Quantity"],columns="count")

print(m1)
print("")
print(m2)
print("")
print(m3)
print("")
print(m33)
print("")
print(m4)
print("")
print(m5)
print("")
print(m6)
print("")
print(m7)
print("")
print(m8)
print("")
print(m9)
print("")
print(m10)
print("")
print(m11)
print("")
