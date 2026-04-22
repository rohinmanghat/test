import matplotlib.pyplot as plt
import numpy as np
# a=np.array([1,2,3,4,5])
# b=np.array([10,20,30,40,50])
# plt.bar(a,b)
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.title("Bar Graph")
# plt.show()
# a=["Aakash","Aryan","Rohin"]
# b=[50,60,50]
# plt.bar(a,b)
# plt.xlabel("Name")
# plt.ylabel("Marks"    )
# plt.title("Bar Graph")
# plt.show()    
x=np.linspace(0,10,100)
y=np.sin(x)
plt.plot(x,y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Sine Wave")
plt.show() 