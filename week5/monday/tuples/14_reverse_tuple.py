def find_repeated(n):
    l = len(n)+1
    list1 = []

    for i in range(-1 , -l , -1):
        list1.append(n[i])

    return tuple(list1)


numbers = (10, 20, 30, 40, 50)

obj = find_repeated(numbers)

print("Reversed tuple:", obj)