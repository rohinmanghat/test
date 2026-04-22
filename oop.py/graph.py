import matplotlib.pyplot as plt

#Line graph
students=["Aakash","Aryan","Rohin","Shreya","Adith"]
marks=[75,60,77,86,60]
plt.plot(students, marks, marker='o')
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks")
plt.show()

#Pie chart
students=["Aakash","Aryan","Rohin","Shreya","Adith"]
marks=[75,60,77,86,60]
plt.pie(marks, labels=students, autopct='%1.1f%%')
plt.title("Student Marks Distribution")
plt.show()

#Bar graph
students=["Aakash","Aryan","Rohin","Shreya","Adith"]
marks=[75,60,77,86,60]
plt.bar(students, marks)
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks")
plt.show()

#Scatter plot
students=["Aakash","Aryan","Rohin","Shreya","Adith"]
marks=[75,60,77,86,60]
plt.scatter(students, marks)
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks")
plt.show()