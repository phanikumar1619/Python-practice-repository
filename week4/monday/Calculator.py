class Calculator():

    calculator_name = "Basic Calculator"

    def display_info(self):
        print("Welcome to Python Calculator")

    @staticmethod
    def add(a , b):
        res = a + b
        print("Addition:",res)

    @staticmethod
    def subtract(a, b):
        if(a < b):
            res = b-a
            print("Subtraction:",res)
        else:
            res = a - b
            print("Subtraction:", res)

    @staticmethod
    def multiply(a, b):
        res = a * b
        print("Multiplication:",res)

    @staticmethod
    def divide(a, b):
        if(b == 0):
            print("Anything divided by 0 is undefined")
        else:
            res = a / b
            print("Division:",res)
    @classmethod
    def change_name(cls , name):
        cls.calculator_name = name

c1 = Calculator()

c1.display_info()

Calculator.add(20, 10)
Calculator.subtract(20, 10)
Calculator.multiply(20, 10)
Calculator.divide(20, 10)

Calculator.change_name("Scientific Calculator")

print(Calculator.calculator_name)