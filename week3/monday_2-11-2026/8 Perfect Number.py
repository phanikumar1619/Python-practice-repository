def perfect(n):
    sum = 0
    for i in range(1 , n):
        if(n%i == 0):
            sum += i
    return sum

n = int(input("Enter the N value :"))

if(perfect(n) == n):
    print("number is perfect number")
else:
    print("number is not perfect number")