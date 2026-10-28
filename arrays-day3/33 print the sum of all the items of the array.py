n = int(input("Enter the N value: "))

a = []

for i in range(n):
    val = int(input("Enter the value for the array: "))
    a.append(val)

sum = 0

for i in range(n):
    sum += a[i]

print(sum)
        