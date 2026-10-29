n = int(input("Enter the N value :"))

total = 0
count = 0

for i in range(1 , n+1):
    y = 1/pow(i , count)
    total += y
    print(y)
    count += 1

print("total sum is",total)