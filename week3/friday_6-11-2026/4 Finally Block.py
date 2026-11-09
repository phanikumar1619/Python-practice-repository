a = int(input("Enter the A value: "))
b = int(input("Enter the B value: "))

try:
    result = a/b
    print("Result:",result)
except ZeroDivisionError as e:
    print("Error:",e)
finally:
    print("This block always executes.")
print("Program execution completed.")