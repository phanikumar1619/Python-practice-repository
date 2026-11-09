a = input("Enter the A value: ")
b = input("Enter the B value: ")

try:
    a = int(a)
    b = int(b)
    try:
        result = a/b
        print("Result:",result)
    except ZeroDivisionError as e:
        print("Error:",e)
except ValueError as e:
    print("Error:",e)

print("Program execution completed.")