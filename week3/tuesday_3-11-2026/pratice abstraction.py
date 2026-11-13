from abc import ABC , abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def calculate_area(self):
#         pass

# class Rectangle(Shape):
#     def calculate_area(self):
#         l = int(input("Enter rectangle length:"))
#         b = int(input("Enter rectangle breadth:"))
#         res = l * b
#         print("Rectangle Area:", res)

# class Circle(Shape):
#     def calculate_area(self):
#         r = int(input("Enter circle radius:"))
#         res = 3.14 * r * r
#         print("Circle Area:", res)

# a = Rectangle()
# b = Circle()

# a.calculate_area()
# b.calculate_area()





# using methods



# class Employee(ABC):
#     @abstractmethod
#     def calculate_salary(self):
#         pass

# class FullTimeEmployee(Employee):
#     def calculate_salary(self):
#         name = input("Enter full-time employee name:")
#         sal = int(input("Enter monthly salary:"))

#         print("Full-Time Employee:",name)
#         print("Monthly Salary:", sal)

# class PartTimeEmployee(Employee):
#     def calculate_salary(self):
#         name = input("Enter part-time employee name:")
#         hour = int(input("Enter hours worked:"))
#         rate = int(input("Enter hourly rate:"))
#         sal = hour * rate
        
#         print("part-time employee:",name)
#         print("Monthly Salary:", sal)


# a = FullTimeEmployee()
# b = PartTimeEmployee()

# a.calculate_salary()
# b.calculate_salary()



# using the Constructor

class Employee(ABC):

    def __init__(self , name):
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):

    def __init__(self, name , sal):
        super().__init__(name)
        self.sal = sal

    def calculate_salary(self):

        print("Full-Time Employee:",self.name)
        print("Monthly Salary:", self.sal)

class PartTimeEmployee(Employee):

    def __init__(self, name , hour , rate ):
        super().__init__(name)
        self.hour = hour
        self.rate = rate

    def calculate_salary(self):
        sal = self.hour * self.rate
        
        print("part-time employee:",self.name)
        print("Monthly Salary:", sal)


a = FullTimeEmployee("phani" , 30000)
b = PartTimeEmployee("kumar" , 80 , 200)

a.calculate_salary()
b.calculate_salary()