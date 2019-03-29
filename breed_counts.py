import numpy as np
import pandas as pd

import matplotlib.mlab as mlab
import matplotlib.pyplot as plt



df_train = pd.read_csv('train.csv')
df_breed = pd.read_csv('breed_labels.csv')

train=pd.DataFrame(df_train)

b1 = pd.crosstab(index=train["Breed1"],columns="count")
b1=pd.DataFrame(b1)
b1.index.name = 'BreedID'

b2 = pd.crosstab(index=train["Breed2"],columns="count")
b2=pd.DataFrame(b2)
b2.index.name = 'BreedID'

breed=pd.DataFrame(df_breed)

type = [[1,"Dog"], [2,"Cat"]]
pet = pd.DataFrame(type, columns = ['Type','Animal'])


b1 = b1.merge(breed,on='BreedID')
results1 = b1.merge(pet,on='Type')

b2 = b2.merge(breed,on='BreedID')
results2 = b2.merge(pet,on='Type')

r1 = results1[['Animal','BreedName','count']]
r2 = results2[['Animal','BreedName','count']]

print("-------------------")
print("")
print("Breed1 data")
with pd.option_context('display.max_rows',9999):
	print(r1)
print("")
print("-------------------")
print("")
print("Breed2 data")
with pd.option_context('display.max_rows',9999):
	print(r2)
print("-------------------")
