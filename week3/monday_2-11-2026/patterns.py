# n = int(input("Enter the N value :"))

# for i in range(n):
#     print("*",end = "\n")




# space = 7
# print("1 " * space)
# print(" " * space ,end = "1")
#print("*" * 7)





# n = int(input("Enter the N value :"))

# for i in range(n):
#     print("*",end = " ")

# n = int(input("Enter the N value :"))

# for i in range(n):
#     for j in range(n):  
#         print("*", end = " ")
#     print()

# n = int(input("Enter the N value :"))

# for i in range(n):
#     for j in range(i+1):  
#         print("*", end = " ")
#     print()


# n = int(input("Enter the N value :"))

# for i in range(n):
#     for j in range(1 , (n+1)-i):  
#         print("*", end = " ")
#     print()

# n = int(input("Enter the N value :"))

# for i in range(1 , n+1):
#     for j in range(1 , i+1):  
#         print(j, end = " ")
#     print()

# n = int(input("Enter the N value :"))

# for i in range(1 , n+1):
#     for j in range(1 , i+1):  
#         print(i, end = " ")
#     print()

# n = int(input("Enter the N value :"))

# for i in range(1 , n+1):
#     for j in range(1 , (n+2)-i):  
#         print(j, end = " ")
#     print()

# n = int(input("Enter the N value :"))
# count = n
# for i in range(1 , n+1):
#     for j in range(1 , (n+2)-i):  
#         print(count, end = " ")
#     count -= 1
#     print()

# n = int(input("Enter the N value :"))
# space = 0
# for i in range(1 , n+1):
#     space = n - i
#     print(" " * space, end = "")
#     for j in range(1 ,i+1):
#         print("*", end = "")
#     print()

# n = int(input("Enter the N value :"))
# space = 0
# for i in range(1 , n+1):
#     space = n - i
#     print(" " * space, end = "")
#     for j in range(1 ,i+1):
#         print("*", end = " ")
#     print()



#method 1 for this pattern

#     *
#    ***
#   *****
#  *******
# *********

# n = int(input("Enter the N value :"))

# space = 0
# star = 0
# for i in range(1 , n+1):
#     space = n - i
#     print(" " * space, end = "")
#     for j in range(i , i+1):
#         star = 2 * i - 1
#         print("*" * star, end = "")
#     print()


#method 2 for this pattern

#     *
#    ***
#   *****
#  *******
# *********

# space = 0
# star = 0
# for i in range(1 , n+1):
#     space = n - i
#     print(" " * space, end = "")
#     star = 2 * i - 1
#     print("*" * star, end = "")
#     print()





# n = int(input("Enter the N value :"))

# space = 0
# star = 0
# for i in range(1 , n+1):
#     space = i
#     print(" " * space , end = "")
#     star = 2*(n-i) + 1
#     print("*" * star)
# print()




# n = int(input("Enter the n value :"))

# space1 = 0
# star1 = 0
# for i in range(1 , n+1):
#     space1 = n - i
#     print(" " * space1, end = "")
#     star1 = 2*i-1
#     print("*" * star1)
# space2 = 0
# star2 = 0
# for i in range(2 , n+1):
#     space2 = i-1
#     print(" " * space2,end = "")
#     star2 = 2*(n-i) + 1
#     print("*" * star2)
# print()





n = int(input("Enter the n value :"))

leadspace1 = 0
innerspace1 = 1

# Upper Hollow Pyramid
for i in range(1, n + 1):
    leadspace1 = n - i
    print(" " * leadspace1, end="")

    if i == 1:
        print("*")
    else:
        print("*", end="")
        print(" " * innerspace1, end="")
        print("*")
        innerspace1 += 2

# Lower Hollow Pyramid
leadspace2 = 0
innerspace2 = innerspace1 - 4

for i in range(1, n):
    leadspace2 = i
    print(" " * leadspace2, end="")

    if i == n - 1:
        print("*")
    else:
        print("*", end="")
        print(" " * innerspace2, end="")
        print("*")
        innerspace2 -= 2

print()