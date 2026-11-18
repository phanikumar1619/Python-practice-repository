def sum_of_list(n):
    # numbers = [10, 20, 30, 40, 50]


    numbers = []
    for i in range(n):
        val = int(input("Enter the value:"))
        numbers.append(val)

    sum = 0
    for i in range(len(numbers)):
        sum += numbers[i]

    print("Sum of elements:", sum)


n = int(input("Enter the value of N:"))
a = sum_of_list(n)