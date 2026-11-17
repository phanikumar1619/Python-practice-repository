def fibonacci_generator():
    num = int(input("Enter number of terms:"))

    count = 0
    a = 0
    b = 1

    while(num > count):
        re = a
        val = a + b
        a = b
        b = val
        count += 1
        yield re

gen = fibonacci_generator()

for i in gen:
    print(i)