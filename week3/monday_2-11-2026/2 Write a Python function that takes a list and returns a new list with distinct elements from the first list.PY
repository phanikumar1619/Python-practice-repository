def distinct(list1):
    list2 = []
    for i in list1:
        if i not in list2:
            list2.append(i)
    return list2

n = int(input("enter the N value :"))
list1 = []

for i in range(n):
    val = int(input("enter the list value :"))
    list1.append(val)

tex = distinct(list1)
print(tex)