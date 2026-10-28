n = int(input("Enter the N vaule: "))

a = 0
b = 1
count = 0

while(n > 0):
    print(a, end="," if n > 1 else "\n")


    sum = a + b
    a = b
    b = sum

    count += 1
    n -= 1