n = int(input("Enter the number: "))
sum = 0 
if(n%2 == 0):
    for i in range(0 , n+1):
        if(i % 2 == 0):
            sum = sum + i
else:
    for i in range(0 , n):
        if(i % 2 == 0):
            sum = sum + i

print("the even number is:", sum)