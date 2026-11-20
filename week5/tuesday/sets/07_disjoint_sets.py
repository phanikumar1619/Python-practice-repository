# A = {10, 20, 30}
# B = {40, 50, 60}

# A.isdisjoint(B)


A = {10, 20, 30, 40, 50}
B = {60, 70, 80, 90}
C = {30, 40, 50, 100}

print("Are A and B disjoint?",A.isdisjoint(B))
print("Are A and C disjoint?",A.isdisjoint(C))
set1 = A.intersection(C)
print("Common elements of A and C:",set1)

C.remove(30)
C.remove(40)
C.remove(50)

print("After removing common elements from C:")

print("Are A and C disjoint?",A.isdisjoint(C))

B.add(20)

print("After adding 20 to B:")

print("Are A and B disjoint?",A.isdisjoint(B))