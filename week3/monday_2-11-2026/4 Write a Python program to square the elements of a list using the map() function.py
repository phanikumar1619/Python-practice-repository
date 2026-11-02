n = int(input("Enter the number of elements :"))
list1 = []

for i in range(n):
    val = int(input("Enter the {} elements:".format(i)))
    list1.append(val)

def square(list1):
    n = list1*list1
    return n

sqea = list(map(square,list1))

print(sqea)