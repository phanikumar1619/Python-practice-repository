class Person:

    def __init__(self , name):
        self.name = name

    def display_person(self):
        print("Person Name:", self.name)

class Student(Person):

    def __init__(self, name , roll_number , employee_id):
        super().__init__(name , employee_id = employee_id)
        self.roll_number = roll_number

    def display_student(self):
        #print("Student Name:", self.name)
        print("Student roll_number:", self.roll_number)

class Employee(Person):

    def __init__(self, name , employee_id):
        super().__init__(name)
        self.employee_id = employee_id

    def display_employee(self):
        print("Employee Id:", self.employee_id)

class TeachingAssistant(Student, Employee):
    def __init__(self, name, roll_number , employee_id):
        super().__init__(name, roll_number , employee_id)

    def display_ta(self):
        print("Name:" , self.name)
        print("Roll_number:" , self.roll_number)
        print("Employee Id:", self.employee_id)

a = TeachingAssistant("phani" , 2200032947 , 123456)
a.display_ta()
a.display_student()
a.display_employee()
a.display_person()