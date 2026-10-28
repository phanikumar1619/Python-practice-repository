m = int(input("Enter the value of M: "))
n = int(input("Enter the value of N: "))

for i in range(m , n+1):
    sum = 0
    for j in range(1 , i):
        if(i%j == 0):
            sum += j
    if(sum == i):
        print("The perfect number is:",i)


# for i in range(1 , n):
#     if(n%i == 0):
#         sum = sum + i 
# print(sum)

# if(sum == n):
#     print("the number is perfect")