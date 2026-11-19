def find_repeated(n):
    list1 = []

    for i in n:
        count = n.count(i)

        if count == 1:
            list1.append(i)

    return tuple(list1)


numbers = (10, 20, 30, 20, 40, 10, 50, 60)

obj = find_repeated(numbers)

print("Non-repeated elements:", obj)