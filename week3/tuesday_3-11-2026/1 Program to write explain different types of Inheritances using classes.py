'''1. Single Inheritance
Concept: One child class inherits from one parent class.


Practice Question 1: Employee and Developer

Create a class Employee with a method work() that prints:
Employee is working

Create a child class Developer that inherits from Employee.

Add a method coding() inside Developer that prints:
Developer is writing Python code

Create an object of Developer and call both methods.


Expected Output
Employee is working
Developer is writing Python code'''


class Employee:
    def work(self):
        print("Employee is working")

class Developer(Employee):
    def coding(self):
        print("Developer is writing Python code")

obj = Developer()
obj.coding()
obj.work()





'''
2. Multiple Inheritance
Concept: One child class inherits from two or more parent classes.


Practice Question 2: Father and Mother
Create a class Father with a method father_property() that prints:
Father owns a house

Create a class Mother with a method mother_property() that prints:
Mother owns gold

Create a child class Child that inherits from both Father and Mother.

Create an object of Child and call both methods.



Expected Output
Father owns a house
Mother owns gold
'''

class Father:
    def father_property(self):
        print("Father owns a house")

class Mother:
    def mother_property(self):
        print("Mother owns gold")

class Child(Father , Mother):
    def child_property(self):
        print("child is bad")


obj = Child()
obj.child_property()
obj.mother_property()
obj.father_property()




'''
3. Multilevel Inheritance
Concept: A class inherits from a child class, forming a chain.

Practice Question 3: Person, Employee, Manager
Create the following classes:
- Person → method details()
- Employee → inherits from Person, method work()
- Manager → inherits from Employee, method manage()
Each method should print a message.

Create an object of Manager and call all three methods.


Expected Output
Person details
Employee is working
Manager is managing the team
'''

class Person:
    def details(self):
        print("Person details")
class Employee(Person):
    def work(self):
        print("Employee is working")
class Manager(Employee):
    def manage(self):
        print("Manager is managing the team")

obj = Manager()
obj.details()
obj.work()
obj.manage()


'''
4. Hierarchical Inheritance
Concept: Multiple child classes inherit from the same parent class.

Practice Question 4: Animal, Dog, Cat
Create a parent class Animal with a method eat() that prints:
Animal is eating

Create two child classes:
- Dog with method bark()
- Cat with method meow()
Both classes should inherit from Animal.

Create objects of Dog and Cat and call their respective methods and the inherited eat() method.

Expected Output
Animal is eating
Dog is barking
Animal is eating
Cat is meowing
'''

class Animal:
    def eat(self):
        print("Animal is eating")
class Dog(Animal):
    def bark(self):
        print("dog is barking")
class Cat(Animal):
    def meow(self):
        print("cat is meowing")

a = Dog()
b = Cat()

a.eat()
a.bark()

b.eat()
b.meow()





'''
5. Hybrid Inheritance
Concept: Hybrid inheritance is a combination of two or more inheritance types.

Practice Question 5: Person, Student, Employee, WorkingStudent
Create the following classes:
- Person → method person_details()
- Student → inherits from Person, method study()
- Employee → inherits from Person, method work()
- WorkingStudent → inherits from both Student and Employee, method balance()
Create an object of WorkingStudent and call all four methods.


Expected Output
Person details
Student is studying
Employee is working
Working student is balancing study and work
'''

class Person:
    def details(self):
        print("Person details")
class Student(Person):
    def study(self):
        print("Student is studying")
class Employee(Person):
    def work(self):
        print("Employee is working")
class WorkingStudent(Student , Employee):
    def balance(self):
        print("Working student is balancing study and work")


b = WorkingStudent()
b.details()
b.study()
b.work()
b.balance()