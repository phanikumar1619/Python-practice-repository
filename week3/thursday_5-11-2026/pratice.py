# def greet():
#     print("Welcome to Python")

# def execute(func):
#     func()

# execute(greet)


# def outer():
#     def inner():
#         print("I am the inner function")
#     return inner()

# outer()


# def outer():
#     def inner():
#         print("Python Decorators")
#     return inner()

# a = outer()
# print(a)


# def outer():
#     def inner():
#         print("I am the inner function")
#     return inner

# a = outer()
# print(a)
# a()


# def decoratordecorator(func):
#     def wrapper():
#         print("Starting execution")
#         func()
#         print("Execution completed")
#     return wrapper

# def python_class():
#     print("Learning Python Decorators")

# a = decoratordecorator(python_class)
# a()








# def mainfunc(func):
#     def wapper():
#         print("----- START -----")
#         func()
#         print("----- END -----")
#     return wapper

# @mainfunc
# def display():
#     print("Welcome to Python Training")

# display()






# def mainfunc(func):
#     def wapper(*args):
#         print("----- START -----")
#         func(*args)
#         print("----- END -----")
#     return wapper

# @mainfunc
# def display(name, course):
#     print(f"Welcome {name}, you are learning {course}")

# display("Phani", "Python Decorators")






def execution_decorator(func):
    def wapper(*args , **kwargs):
        print("Execution Started")
        func(*args , **kwargs)
        print("Execution Finished")
    return wapper

@execution_decorator
def student(name, course):
    print(f"Student Name: {name}")
    print(f"Course: {course}")

student("Phani", "Python")


@execution_decorator
def employee(name, salary, department):
    print(f"Employee: {name}")
    print(f"Salary: {salary}")
    print(f"Department: {department}")

employee(name="Phani", salary=30000, department="IT")

@execution_decorator
def calculate(a, b, operation):
    if operation == "add":
        print(a + b)
    elif operation == "multiply":
        print(a * b)

calculate(10, 20, operation="add")
calculate(10, 20, operation="multiply")