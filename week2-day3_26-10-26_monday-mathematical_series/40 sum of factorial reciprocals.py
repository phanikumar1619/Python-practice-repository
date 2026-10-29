n = int(input("Enter the N value :"))

def fac(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * fac(n-1)

total = 0

for i in range(1 , n+1):
    y = 1/fac(i)
    total += y
    print(y)

# total = fac(n)

print("total sum is",total)

# same as question 42 but it should only print n = 4