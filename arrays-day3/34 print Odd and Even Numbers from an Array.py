n = int(input("Enter the N value: "))

a = []
odd = []
even = []

for i in range(n):
    val = int(input("Enter the value for the array: "))
    a.append(val)


for i in range(n):
    if(a[i]%2 == 0):
        even.append(a[i])
    else:
        odd.append(a[i])

print("even numbers :",even)
print("odd numbers :",odd)