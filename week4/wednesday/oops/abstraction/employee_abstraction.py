from abc import ABC , abstractmethod

class Employee(ABC):
    def __init__(self , employee_name , employee_id):
        self.employee_name = employee_name
        self.employee_id = employee_id

    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, employee_name, employee_id , salary):
        super().__init__(employee_name, employee_id)
        self.salary = salary

    def calculate_salary(self):
        return self.salary

    def display_details(self):
            print("Employee Name:", self.employee_name)
            print("Employee ID:", self.employee_id)
            print("Employee Salary:", self.calculate_salary())

class PartTimeEmployee(Employee):
    def __init__(self, employee_name, employee_id , rate , hours):
        super().__init__(employee_name, employee_id)
        self.rate = rate
        self.hours = hours

    def calculate_salary(self):
        return self.rate * self.hours


    def display_details(self):
            print("Employee Name:", self.employee_name)
            print("Employee ID:", self.employee_id)
            print("Employee Salary:", self.calculate_salary())

full_time = FullTimeEmployee("Phani", 101, 40000)
full_time.display_details()
full_time.calculate_salary()

part_time = PartTimeEmployee("Pavan", 102, 500, 80)
part_time.display_details()
part_time.calculate_salary()
    