class Person:
    def __init__(self , name , age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Person Name:" , self.name)
        print("Person Age:" , self.age)

class Student(Person):
    def __init__(self, name, age , roll_number):
        self.name = name
        self.age = age
        self.roll_number = roll_number

    def display_student(self):
        print("Person Name:" , self.name)
        print("Person Age:" , self.age)
        print("Person Roll_number:" , self.roll_number)

student = Student("Phani", 22, 101)

student.display_person()
student.display_student()
