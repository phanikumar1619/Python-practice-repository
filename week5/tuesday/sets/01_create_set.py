set1 = {5, 10, 15, 10, 20, 25, 15, 30, 5, 35}

elements = len(set1)
print("Unique elements:",elements)

def obj():
    if 25 in set1:
        return True
    else:
        return False

a = obj()

def obj1():
    if 100 in set1:
        return True
    else:
        return False

b = obj1()

print("Is 25 present?",a)
print("Is 100 present?",b)

set1.add(40)
print("After adding 40:",set1)
set1.remove(10)
print("After removing 10:",set1)