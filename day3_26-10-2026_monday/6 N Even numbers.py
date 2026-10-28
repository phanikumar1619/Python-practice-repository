# n = int(input("Enter the N value"))
# if(n%2 == 0):
#     for index,i in enumerate(range(1 , (n * 2)+1)):
#         if(i % 2 == 0):
#             print("the even number is: ", i)

# else:
#     for index,i in enumerate(range(1 , n * 2)):
#         if(i % 2 == 0):
#             print("the even number is: ", i)


n = int(input("Enter the N value: "))
count = 1

if n % 2 == 0:
    for i in range(1, (n * 2) + 1):
        if i % 2 == 0:
            print("the {} number is : {}".format(count, i))
            count += 1
else:
    for i in range(1, n * 2):
        if i % 2 == 0:
            print("the {} number is : {}".format(count, i))
            count += 1
