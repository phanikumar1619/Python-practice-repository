# n = int(input("Enter the N value :"))

list1 = [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]


# for i in range(n):
#     val = int(input("Enter the element :"))
#     list1.append(val)


clean_data = list(filter(lambda x: x is not None, list1))


print(clean_data)