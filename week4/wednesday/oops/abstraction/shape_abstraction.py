from abc import ABC , abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):

    def __init__(self , length , breadth):
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        area = self.length * self.breadth
        print("Area of Rectangle:", area)

class Circle(Shape):

    def __init__(self , radius):
        self.radius = radius

    def calculate_area(self):
        area = 3.14 * self.radius * self.radius
        print("Area of Circle:", area)

rectangle = Rectangle(10, 5)
circle = Circle(7)

rectangle.calculate_area()
circle.calculate_area()