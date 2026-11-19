
numbers = (10, 20, 30, 20, 40, 10, 50, 60)
tup = list(numbers)
tup.sort()

l = len(tup)

for i in range(l):
    count = 1
    if i > 0 and tup[i] == tup[i-1]:
        continue
    for j in range(i+1 , l):
        if tup[i] == tup[j]:
            count += 1
    print(f"{tup[i]} occurs {count} times")