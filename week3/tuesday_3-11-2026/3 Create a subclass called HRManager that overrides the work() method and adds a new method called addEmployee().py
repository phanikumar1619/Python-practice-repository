'''
Create a subclass called HRManager that overrides the work() method and
adds a new method called addEmployee().
'''

class Employee:
    def work(self):
        print("Employee is working")
class HRManager(Employee):
    def work(self):
        print("HRManager is working")
    def addEmployee(self):
        print("new employee is added")

a = HRManager()
a.work()
a.addEmployee()
b = Employee()
b.work()
