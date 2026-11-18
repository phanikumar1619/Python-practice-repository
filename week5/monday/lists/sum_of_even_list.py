def sum_of_list(n):
    # numbers = [10, 20, 30, 40, 50]


    numbers = []
    for i in range(n):
        val = int(input("Enter the value:"))
        numbers.append(val)

    total = 0
    for i in range(n):
        if numbers[i]%2 == 0:
            total += numbers[i]

    print("Sum of even elements:", total)


n = int(input("Enter the value of N:"))
a = sum_of_list(n)