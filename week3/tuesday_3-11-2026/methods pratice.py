class Calculator():

    @staticmethod
    def add(a , b):
        result = a + b
        print("Addition: ", result)

    @staticmethod
    def multiply(a , b):
        mul = a * b
        print("Multiplication: ",mul)

c = Calculator()
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c.add(a , b)
c.multiply(a ,b)