set1 = {10, 20, 30, 40, 50, 60, 70}
set2 = {30, 40, 50, 60, 80, 90}

set3 = set1.intersection(set2)
print("Common elements:",set3)

length = len(set3)

print("Total common elements:",length)

def obj():
    if 30 in set3:
        return True
    else:
        return False

a = obj()

def obj1():
    if 100 in set3:
        return True
    else:
        return False

b = obj1()

print("Is 30 common?",a)
print("Is 100 common?",b)

set1.add(100)
print("After adding 100 to Group A:")
print("Common elements:",set3)