def remove_common(list1, list2):

    list3 = []
    list4 = []

    for i in list1:
        if i not in list2:
            list3.append(i)
    
    for i in list2:
        if i not in list1:
            list4.append(i)

    print("List 1 after removing common elements:",list3)
    print("List 2 after removing common elements:",list4)
        


# n = int(input("Enter the size of list1:"))
# list1 = []
# list2 = []

# for i in range(n):
#     val = int(input("Enter the value of list1"))
#     list1.append(val)

# m = int(input("Enter the size of list2:"))

# for i in range(m):
#     val = int(input("Enter the value of list2"))
#     list2.append(val)

list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 60, 70]

a = remove_common(list1 , list2)