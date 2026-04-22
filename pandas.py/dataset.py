import pandas as pd
name=["Rohin","Aakash","Aryan","Shreya","Hari","Adith","Adithyan","Adwaith","Sreehari","Sidharth"]
marks=[90,85,88,92,80,95,89,91,87,93]
dict1={"Name":name,"Marks":marks}
df=pd.DataFrame(dict1,index=["A","B","C","D","E","F","G","H","I","J"])
print(df)
print("")
print(df.loc["G"])
