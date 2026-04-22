import pandas as pd
import numpy as np
#Series of list
l1=[1,2,3,4,5]
l2=['a','b','c','d','e']
s1=pd.Series(l1, index=l2)
print(s1)
print("")
#Series of dictionary
dict1={"Rohin":"Hunter","Aakash":"RXZ","Aryan":"Hornet"}
s2=pd.Series(dict1)
print(s2)
print("")
#Series of numpy array
lst1=np.array([1,2,3,4,5])
s3=pd.Series(lst1)
print(s3)