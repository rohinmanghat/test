import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data.csv", sep=";")
print(df)
print("")
plt.bar(df["Name"],df["Marks"])
plt.xlabel("Name")
plt.ylabel("Marks")
plt.title("Marks of students")
plt.show()