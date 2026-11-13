class BankEmployee():
    bank_name = "SBI"
    employee_count = 0

    def __init__(self , name , employee_id , salary):
        if(salary <= 0):
            print("rejected")
        else:
            self.name = name 
            self.employee_id = employee_id
            self.salary = salary
            BankEmployee.employee_count += 1

    def display_details(self):
        print("Employee Name:",self.name)
        print("Employee ID:",self.employee_id)           
        print("Employee Salary:",self.salary)
        print("Bank Name:", self.bank_name)
        print()

    def calculate_bonus(self , percentage):
        if self.salary <= 0 or (percentage < 0 or percentage > 100):
            print("rejected")
        else:
            bonus = self.salary * (percentage/100)
            return bonus

    @classmethod
    def change_bank_name(cls , new_name):
        cls.bank_name = new_name

    @staticmethod
    def is_eligible_for_loan(salary):
        if(salary <= 0):
            return False
        elif(salary >= 30000):
            return True
        else:
            return False


e1 = BankEmployee("Phani", 101, 40000)
e2 = BankEmployee("Rahul", 102, 25000)
e3 = BankEmployee("Kumar", 103, 50000)

# e1.display_details()

print("Bonus:", e1.calculate_bonus(101))

# print(BankEmployee.is_eligible_for_loan(40000))
# print(BankEmployee.is_eligible_for_loan(-20000))

# BankEmployee.change_bank_name("HDFC")

# print("Total Employees:", BankEmployee.employee_count)