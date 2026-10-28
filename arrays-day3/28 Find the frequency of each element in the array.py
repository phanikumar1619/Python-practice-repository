n = int(input("Enter the N value: "))
f = int(input("Enter the number to find: "))
count = 0


a = []
for i in range(n):
    val = int(input("Enter the value for the array: "))
    a.append(val)

for i in range(n):
    if(a[i] == f):
        count += 1

print(a)
print("The number {} is find {} times in the arry".format(f,count))