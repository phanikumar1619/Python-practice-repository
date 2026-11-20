A = {10, 20, 30, 40, 50, 60}
B = {40, 50, 60, 70, 80, 90}

print("Union:", A | B)
print("Intersection:", A & B)
print("A - B: ", A - B)
print("B - A: ", B - A)
print("Symmetric Difference:", A ^ B)

print("Are A and B disjoint?",A.isdisjoint(B))