class Shape:
    def __init__(self , radius):
        self.radius = radius
    def area(self):
        print("Area of shape")
class Circle(Shape):
    def area(self):
        area1 = 3.14 * self.radius *self.radius
        print("Area of circle is :",area1)
a = Circle(7)
a.area()
b = Shape(0)
b.area()



class Vehicle:
    def __init__(self , brand , speed):
        self.brand = brand
        self.speed = speed
    def displayInfo(self):
        print("Brand:",self.brand)
        print("Speed:",self.speed)
class Car(Vehicle):
    def displayInfo(self):
        super().displayInfo()
        print("This is car")

a = Car("Toyota" , "120 km/h")
a.displayInfo()