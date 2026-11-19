# def find_repeated(n):
#     for i in n:
#         for j in i:
#             n[len(i)] = 100

#     return tuple(n)


# numbers = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

# obj = find_repeated(numbers)

# print("Reversed tuple:", obj)

# size1 = len(numbers)
# for i in range(size1):
#     size2 = len(i)
#     print(size2)
#     for j in range(size2):
#         i[size2-1] = 100
    

# print(numbers)



def replace_last_value(n):
    list1 = []

    for i in n:
        new_tuple = i[:-1] + (100,)
        list1.append(new_tuple)

    return list1


numbers = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

result = replace_last_value(numbers)
print("Updated list:", result)