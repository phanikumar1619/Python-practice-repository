n = int(input("Enter the N value: "))

a = []

for i in range(n):
    val = int(input("Enter the value for the array: "))
    a.append(val)

large = a[0]
temp = 0

for i in range(n):
    for j in range(i+1, n):
        if(a[i] < a[j]):
            temp = a[i]
            a[i] = a[j]
            a[j] = temp

print(a)
        