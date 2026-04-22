# x="hello world"
# y=("12","hi",-1,2.5)
# z=("99.99","hello")
# print(len(x))
# print(len(y))
# print(len(z))
# g={"name":"Aakash","age":20,"course":"BBA"}
# print(len(g))


# x="Hoiii"
# y=5
# print(x*5)
# print(y*5)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
p1 = Person("Aakash", 20)
print(p1.name)
print(p1._Person__age)
