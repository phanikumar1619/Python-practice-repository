set1 = {10, 20, 30, 40, 50, 60, 70}
set2 = {30, 40, 50, 80, 90, 100}

set3 = set1.symmetric_difference(set2)
print("Symmetric difference:",set3)

length = len(set3)
print("Total elements:",length)

def obj():
    if 20 in set3:
        return True
    else:
        return False

a = obj()

def obj1():
    if 40 in set3:
        return True
    else:
        return False

b = obj1()

print("Is 20 present?",a)
print("Is 40 present?",b)


print("After modifying the groups:")

set1.add(110)
set2.remove(90)

set3 = set1.symmetric_difference(set2)
print("Symmetric difference:",set3)

length = len(set3)
print("Total elements:",length)