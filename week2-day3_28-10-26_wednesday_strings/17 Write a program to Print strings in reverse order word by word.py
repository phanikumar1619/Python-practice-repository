n = int(input("Enter the size of string: "))

names = []

for i in range(n):
    vals = input("Enter the value of string: ")
    names.append(vals)

print("Original List:",names)
print("Reversed List:", names[::-1])