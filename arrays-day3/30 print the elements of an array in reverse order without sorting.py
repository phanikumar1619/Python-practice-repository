n = int(input("Enter the N value: "))

a = []
d = 0

for i in range(n):
    val = int(input("Enter the value for the array: "))
    a.append(val)
full = len(a)
for i in range(full-1 , -1 , -1):
    print(a[i], end = ",")