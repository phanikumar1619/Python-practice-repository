set1 = {10, 20, 30, 40, 50, 60, 70, 80}
set2 = {30, 40, 50, 60, 90, 100}

set3 = set1.difference(set2)
print("Elements in A but not B:",set3)
set4 = set2.difference(set1)
print("Elements in B but not A:",set4)

length1 = len(set3)
print("Count of A difference:",length1)
length2 = len(set4)
print("Count of B difference:",length2)

def obj():
    if 20 in set3:
        return True
    else:
        return False

a = obj()

def obj1():
    if 90 in set4:
        return True
    else:
        return False

b = obj1()

print("Is 20 present?",a)
print("Is 90 present?",b)


print("After adding 110 to Group B:")

set2.add(110)

set3 = set1.difference(set2)
print("Elements in A but not B:",set3)
set4 = set2.difference(set1)
print("Elements in B but not A:",set4)