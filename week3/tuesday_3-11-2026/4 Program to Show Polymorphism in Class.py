class Cal:
    def __init__(self , a , b):
        self.a = a
        self.b = b
    def add(self):
        total = self.a + self.b
        print(total)

a = Cal(5 , 10)
a.add()
a = Cal("phani" , "kumar")
a.add()
a = Cal([1 , 2 , 3] , [4 , 5 , 6])
a.add()



class Rectangle:
    def __init__(self, length , breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        area = self.length * self.breadth
        print("Area of Rectangle:",area)

class Circle:
    def __init__(self , radius):
        self.radius = radius
    def area(self):
        area = 3.14 * self.radius * self.radius
        print("Area of Circle:", area)

a = Circle(7)
a.area()
b = Rectangle(4 , 5)
b.area()