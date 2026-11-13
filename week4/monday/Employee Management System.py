class Employee():
    company = "Google"

    def __init__(self , name , employee_id , salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print("employee name:", self.name)
        print("employee Id:",self.employee_id)
        print("employee salary:",self.salary)

    @classmethod
    def change_company(cls , company):
        cls.company = company


e1 = Employee("Phani", 101, 30000)
e2 = Employee("Rahul", 102, 40000)
e3 = Employee("Kumar", 103, 35000)

e1.display_details()
e2.display_details()
e3.display_details()
print(Employee.company)

Employee.change_company("Microsoft")

e1.display_details()
e2.display_details()
e3.display_details()
print(Employee.company)



e1.company = "Amazon"
e1.display_details()
print(e1.company)
e2.display_details()
print(e2.company)
e3.display_details()
print(e3.company)
