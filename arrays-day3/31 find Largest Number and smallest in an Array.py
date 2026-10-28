n = int(input("Enter the N value: "))

a = []

for i in range(n):
    val = int(input("Enter the value for the array: "))
    a.append(val)

small = a[0]
large = a[0]

for i in range(n):
    if(a[i] < small):
        small = a[i]
    elif(a[i] > large):
        large = a[i]

print("The largest number in the array is :",large)
print("The smallest number in the array is :",small)