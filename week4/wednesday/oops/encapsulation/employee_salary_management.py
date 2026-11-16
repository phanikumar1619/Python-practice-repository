class Employee:

    def __init__(self , employee_name):
        self.employee_name = employee_name
        self.__salary = 30000

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self , new_salary):
        if(new_salary < 0 or new_salary > 100000):
            print("Invalid")
        else:
            print("updated successfully")
            self.__salary = new_salary

    def display(self):
        print("Employee Name:",self.employee_name)
        print("Current Salary:" , self.salary)

a = Employee("phani")
a.display()
a.salary = 60000
a.display()
a.salary = 1000000
a.display()