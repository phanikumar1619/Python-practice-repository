n = int(input("Enter the N vaule: "))

sum = 0
for i in range(1 , n):
    if(n%i == 0):
        sum += i

if(sum == n):
    print("The {} is perfect number".format(n))
else:
    print("The {} is not perfect number".format(n))