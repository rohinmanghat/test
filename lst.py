lst1=["Apple","Banana","Cherry","Mango","Grapes"]
print(lst1)
print(lst1[0]) #Accessing the first element
print(lst1[1:4]) #Accessing a range of elements 
print(lst1[:3]) #Accessing the first three elements
lst1.append("Orange") #Adding an element to the end of the list
print(lst1)
lst1.insert(2,"Pineapple") #Inserting an element at a specific index
print(lst1)
lst1.remove("Banana") #Removing an element from the list
print(lst1)
lst1.pop() #Removing the last element from the list
print(lst1)
lst1[1]="Strawberry" #Modifying an element in the list
print(lst1)
print("")

a=("Apple","Banana","Cherry","Mango","Grapes") #Creating a tuple
print(a)