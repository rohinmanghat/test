class Shape:
    def area(self):
        pass
class Square(Shape):
    def __init__(self, side):
        self.side =int(input("Enter the side of square: "))
    def area(self):
        return self.side * self.side    
class Rectangle (Shape):
    def __init__(self,lenght,breadth):
        self.lenght=int(input("Enter the lenght of rectangle: "))
        self.breadth=int(input("Enter the breadth of rectangle: "))
    def area(self):
        return self.lenght*self.breadth
class Circle(Shape):
    def __init__(self,radius):
        self.radius=int(input("Enter the radius of circle: "))
    def area(self):
        return 3.14*self.radius*self.radius
s=Square(4)
r=Rectangle(5,3)
c=Circle(2)
print("Area of square:",s.area())    
print("Area of rectangle:",r.area())
print("Area of circle:",c.area())