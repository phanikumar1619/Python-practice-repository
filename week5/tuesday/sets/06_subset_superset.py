set1 = {10, 20, 30, 40, 50, 60, 70, 80}
set2 = {20, 30, 40}
set3 = {20, 30, 90}


def obj():
    if set2.issubset(set1):
        return True
    else:
        return False

a = obj()

print("Is B a subset of A?",a)

def obj():
    if set1.issuperset(set2):
        return True
    else:
        return False

b = obj()

print("Is A a superset of B?", b)








def obj():
    if set3.issubset(set1):
        return True
    else:
        return False

a = obj()

print("Is C a subset of A?",a)

def obj():
    if set1.issuperset(set3):
        return True
    else:
        return False

b = obj()

print("Is A a superset of C?", b)


set4 = set3.difference(set1)
print("Elements of C missing from A:",set4)


set1.add(90)

print("After adding 90 to A:")

def obj():
    if set3.issubset(set1):
        return True
    else:
        return False

a = obj()

print("Is C a subset of A?",a)

def obj():
    if set1.issuperset(set3):
        return True
    else:
        return False

b = obj()

print("Is A a superset of C?", b)