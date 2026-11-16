class Employee:

    def __init__(self , employee_name , __employee_id):
        self.employee_name = employee_name
        self.__employee_id = __employee_id

    @property
    def employee_id(self):
        return self.__employee_id

    def display(self):
        print("Employee Name:",self.employee_name)
        print("Employee ID:",self.employee_id)

employee = Employee("Phani", 101)

print(employee.employee_id)

employee.display()