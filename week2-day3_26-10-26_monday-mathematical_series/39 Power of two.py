n = int(input("Enter the N value :"))

total = 0
count = 2

for i in range(0 , n+1):
    y = 1/pow(count , i)
    total += y
    print(y)

print("total sum is",total)