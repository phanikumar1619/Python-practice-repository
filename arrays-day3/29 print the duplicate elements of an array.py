n = int(input("Enter the N value: "))

a = []
d = 0

for i in range(n):
    val = int(input("Enter the value for the array: "))
    a.append(val)

for i in range(n-1):
    if(a[i] == a[i+1]):
        d += 1

if(d == 0):
    print("no duplicate values")
else:
    print("{} duplicate values are present".format(d))