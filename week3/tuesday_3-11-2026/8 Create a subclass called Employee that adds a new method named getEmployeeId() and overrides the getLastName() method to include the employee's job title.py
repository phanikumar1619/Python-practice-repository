class Person:
    def getFirstName(self):
        print("phani")
    def getLastName(self):
        print("kumar")

class Employee(Person):
    def getEmployeeId(self):
        print("1002")
    def getLastName(self):
        print("kumar")
        print("software")

a = Employee()
a.getLastName()
a.getFirstName()
a.getEmployeeId()   