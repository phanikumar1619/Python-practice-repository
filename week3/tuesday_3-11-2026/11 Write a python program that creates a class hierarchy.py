# class Employee():
#     def __init__(self , name , address , sal , title):
#         self.name = name
#         self.address = address
#         self.sal = sal
#         self.title = title

#     def detials(self):
#         print("Enter Manager Details:")
#         self.name = input("Enter Name: ")
#         self.address = input("Enter Address: ")
#         self.sal = int(input("Enter Salary: "))
#         self.title = input("Enter Job Title: ")

# class Manager(Employee):
#     def __init__(self, name, address, sal, title):
#         super().__init__(name, address, sal, title)

#     def calculateBonus(self):
#         bonus = self.sal * (20/100)
#         print(bonus)


# a = Manager()
# a.detials()
# a.calculateBonus()



# class Employee:
#     def display_details(self , name , id):
#         self.name1 = name
#         self.id = id
#         print("Employee Name: ", name)
#         print("Employee ID: ", id)

# a = Employee()
# a.display_details("Rahul" , 101)
# a.display_details("Kiran" , 102)
# b = Employee()
# b.display_details("phani" , 2200032947)


class Employee():
    def __init__(self , name , id , salary):
        self.name = name
        self.id = id
        self.salary = salary

    def display_details(self):
        print("Employee Name: ", self.name)
        print("Employee ID: ", self.id)
        print("Employee Salary: ", self.salary)

a = Employee("Rahul", 101, 30000)
b = Employee("Phani", 102, 40000)
c = Employee("Kumar", 103, 35000)

a.display_details()
b.display_details()
c.display_details()