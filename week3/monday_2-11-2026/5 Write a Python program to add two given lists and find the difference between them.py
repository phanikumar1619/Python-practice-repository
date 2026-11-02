n = int(input("Enter the N value :"))

list1 = []
list2 = []

for i in range(n):
    val = int(input("Enter the element :"))
    list1.append(val)

print("Enter the second list elements :")

for i in range(n):
    val = int(input("Enter the element :"))
    list2.append(val)

print("List1 :", list1)
print("List2 :", list2)

def add_sub(a, b):
    addition = a + b
    difference = a - b
    return (addition, difference)

result = list(map(add_sub, list1, list2))

print("Result :", result)