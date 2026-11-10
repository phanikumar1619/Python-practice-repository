row = int(input("Enter the row value: "))
col = int(input("Enter the col value: "))

# for i in range(row):
#     for j in range(col):
#         print("*", end = " ")
#     print()

# for i in range(row):
#     for j in range(i+1):
#         print("*" , end = " ")
#     print()

# for i in range(1 , row+1):
#     for j in range(1 , i+1):
#         print(j , end = " ")
#     print()

# n = row
# for i in range(row):
#     for j in range(n-i):
#         print("*" , end = " ")
#     print()

# n = row
# for i in range(1 , row+1):
#     space = n - i
#     print(" " * space ,end = "")
#     for j in range(i):
#         print("*" , end = "")
#     print()



# Challenge2

# n = row
# for i in range(1 , n+1):
#     for j in range(i , n + 1):
#         print("*" , end = " ")
#     print()


# count = 1
# for i in range(1 , row + 1):
#     for j in range(1 , i + 1):
#         print(count, end = " ")
#         count += 1
#     print()



# n = row + 2
# for i in range(1 , row + 1):
#     for j in range(1 , n - i):
#         print(j , end = " ")
#     print()





# Challenge 3

# n = row
# star = 1
# for i in range(1 , row+1):
#     space = n - i
#     print(" " * space, end = "")
#     print("*" * star, end = " ")
#     star += 2
#     print()





# space = 0
# n = row
# for i in range(1 , row + 1):
#     print(" " * space, end = "")
#     star = 2 * n - 1
#     print("*" * star , end = "")
#     n -= 1
#     space += 1
#     print()








# Upper half of the diamond
# star1 = 1

# for i in range(1, row + 1):
#     space1 = row - i
#     print(" " * space1, end="")

#     print("*" * star1, end="")
#     star1 += 2

#     print()

# Lower half of the diamond
# star2 = star1 - 4

# for i in range(1, row):
#     space2 = i
#     print(" " * space2, end="")

#     print("*" * star2, end="")
#     star2 -= 2

#     print()





# space = row - 2
# for i in range(1 , row + 1):
#     if(i == 1 or i == row):
#         print("*" * row , end = "")
#         print()
#     else:
#         print("*" , end = "")
#         print(" " * space, end = "")
#         print("*", end= "")
#         print()





# for i in range(1 , row + 1):
#     for j in range(1 , col + 1):
#         if i == 1 or i == row or j == 1 or j == col :
#             print("*",end = "")
#         else:
#             print(" ", end = "")
#     print()





# for i in range(1 , row + 1):
#     for j in range(1 , i + 1):
#         if i == 1 or i == row or j == 1 or j == i :
#             print("*" , end = "")
#         else:
#             print(" " , end = "")
#     print()





# for i in range(1 , row+1):
#     space = row - i
#     print(" " * space , end = "")
#     for j in range(1 , i + 1):
#         print(j , end = "")
#         c = j - 1
#     for k in range(1 , i):
#         print( c, end = "")
#         c -= 1
#     print()







# for i in range(1 , row + 1):
#     space1 = row - i
#     print(" " * space1, end = "")
#     for j in range(1 , i + 1):
#         print(j , end = "")
#     c = i - 1
#     for k in range(1 , i):
#         print(c , end = "")
#         c -= 1
#     print()
# space2 = 1
# n = row
# for i in range(1 , row):
#     print(" " * space2 , end = "")
#     for j in range(1 , n):
#         print(j , end = "")
#     c = n - 2
#     for k in range(1 , n-1):
#         print(c , end = "")
#         c -= 1
#     space2 += 1
#     n -= 1
#     print()




# for i in range(1 , row):
#     space1 = row - i
#     print(" " * space1 , end = "")
#     for j in range(space1 , row):
#         print(j , end = "")
#     c = j - 1
#     for k in range(1 , i):
#         print(c , end = "")
#         c -= 1
#     print()

# space2 = 1
# s = 2
# for i in range(1 , row - 1):
#     print(" " * s , end = "")
#     for j in range(space2 + 1 , row):
#         print(j , end = "")
#     c = j - 1
#     n = row - i - 1
#     for k in range(1 , n):
#         print(c , end = "")
#         c -= 1
#     space2 += 1
#     s += 1
#     print()



text = 'hello python world'
result = ''

for i in text:
    if(i == " "):
        print(result)
        result = ""
    else:
        result += i
print(result)