class Employee:

    def __init__(self , name , salary):
        self.name = name
        self.salary = salary

    def display_employee(self):
        print("Employee Name:" , self.name)
        print("Employee Salary:" , self.salary)

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def display_developer(self):
        print("Developer Name:" , self.name)
        print("Developer Salary:" , self.salary)
        print("Developer programming_language" , self.programming_language)

developer = Developer("Phani", 50000, "Python")

developer.display_employee()
developer.display_developer()