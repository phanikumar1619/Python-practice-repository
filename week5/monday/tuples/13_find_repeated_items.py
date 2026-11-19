def find_repeated(n):
    l = len(n) - 1
    list1 = []
    for i in range(l):
        for j in range(i + 1 , l):
            if(n[i] == n[j] and n[i] not in list1):
                list1.append(n[j])
                #print("Repeated elements:")
                #print(n[j],end = ",")
                
    return tuple(list1)



numbers = (10, 20, 30, 20, 40, 10, 50, 20)
tup = list(numbers)
tup.sort()

obj = find_repeated(tup)
print("Repeated elements:", obj)


# def find_repeated(n):
#     l = len(n)
#     list1 = []

#     for i in range(l):
#         for j in range(i + 1, l):

#             if n[i] == n[j]:

#                 if n[i] not in list1:
#                     list1.append(n[i])

#     return tuple(list1)


# numbers = (10, 20, 30, 20, 40, 10, 50, 20)

# obj = find_repeated(numbers)

# print("Repeated elements:", obj)