class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, my name is {self.name} and I am {self.age} years old."
    
    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"
    
p1 = Person("Aakash", 20)
p2 = Person("Aryan", 19)
print(p1.greet())
print(p2.name, p2.age)