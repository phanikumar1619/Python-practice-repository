# Create a class called Student with a method display() that prints "I am a student"



# class Student:
#     print("nice to meet you")
#     def display(self):
#         print("I am a student")

# obj = Student()
# obj.display()







#Create a class called Employee with a method work() that prints "Employee is working". Create two objects and call the method.

# class Employee:
#     def work(self):
#         print("Employee is working")

# obj1 = Employee()
# obj2 = Employee()

# obj1.work()
# obj2.work()







#Create a class called Car with attributes brand and color. Create two objects with different values and display their details.

# class Car:
#     brand = "verna"
#     color = "red"
#     def cardetials(self, brand , color):
#         self.brand = brand
#         self.color = color
#         print(f"The car brand is {self.brand} and The car color is {self.color}")

# obj1 = Car()
# obj2 = Car()

# obj1.cardetials("audi","white")
# obj2.cardetials("verna", "red")






# Create a class called Laptop with attributes brand, price, and ram. Create three objects and display their information.

# class Laptop:
#     brand = "asus"
#     price = 32000
#     ram = 16
#     def display(self , brand , price , ram):
#         self.brand = brand
#         self.price = price
#         self.ram = ram
#         print(f"The laptop brand is {self.brand} , the price is {self.price} , the ram is {self.ram}GB")

# a = Laptop()
# b = Laptop()
# c = Laptop()

# a.display("asus" , 32000 , 16)
# b.display("hp" , 40000 , 8)
# c.display("lenovo" , 50000 , 16)








'''Create a class called BankAccount with methods:
- deposit()
- withdraw()
- displayBalance()
Create an object and perform multiple operations.'''

# class BankAccount:
#     def deposit(self):
#         print("deposit")
#     def withdraw(self):
#         print("withdraw")
#     def displaybalance(self):
#         print("balance")

# a = BankAccount()
# a.deposit()
# a.displaybalance()
# a.withdraw()








'''Question
Create a class called Student.

Requirements:
1. Create a class variable school = "ABC School".
2. Create an instance variable name.
3. Create a method display() to print the student's name and school.
4. Create three objects with different student names.
5. Change the school name using the class.
6. Display the details of all three students.'''

class Student:
    school = "ABC School"
    name = "pasd"
    def __init__(self , name):
        self.name = name
    @classmethod
    def changeschool(cls , school):
        cls.school = school
a = Student("phani")

print("Student Name: " , a.name)
print("School: ",a.school)

a.changeschool("xyz school")

print("Student Name: " , a.name)
print("School: ",a.school)

print(a.school)