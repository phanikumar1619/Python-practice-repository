a = input("Enter the A value: ")
b = input("Enter the B value: ")

try:
    a = int(a)
    b = int(b)
    div = a/b
    print("Output the result:",div)
except ZeroDivisionError as e:
    print("error:",e)
except ValueError as e:
    print("error:",e)
print("Program execution completed.")