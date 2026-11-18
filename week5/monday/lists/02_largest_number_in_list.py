def find_largest(n):

    numbers = []

    for i in range(n):
        val = int(input("Enter the value:"))
        numbers.append(val)

    large = numbers[0]

    for i in range(1 , n):
        if(large < numbers[i]):
            large = numbers[i]

    return large

n = int(input("Enter the value of N:"))

a = find_largest(n)

print("Largest number:",a)