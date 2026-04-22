import pandas as pd
dict1={"Name":["Rohin","Aakash","Aryan"],"Age":[20,21,22],"Course":["BCA","BBA","BCP"]}
df=pd.DataFrame(dict1,index=["Student1","Student2","Student3"])
print(df)