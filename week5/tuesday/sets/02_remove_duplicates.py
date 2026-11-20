set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set3 = set1.union(set2)
print("Combined set:",set3)
length = len(set3)
print("Total unique elements:",length)
def obj():
    if 60 in set3:
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

print("Is 60 present?",a)
print("Is 100 present?",b)

set3.update((80 , 90))
print("After adding:",set3)

set3.remove(20)
print("After removing 20:",set3)