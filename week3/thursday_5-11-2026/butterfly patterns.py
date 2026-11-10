row = int(input("Enter the row value: "))

# for i in range(1 , 2*row):
#     space1 = row - i
#     if(i <= row):
#         for j in range(1 , i+1):
#             print(j, end = "")
#         print(" " * space1 , end = "")
#         print(" " * space1 , end = "")
#         c1 = i
#         for j in range(1 , i + 1):
#             print(c1 , end = "")
#             c1 -= 1
#         print()
#     else:
#         space2 = i - row
#         inner = row - space2
#         for k in range(1 , inner + 1):
#             print(k , end = "")
#         print(" " * space2 , end = "")
#         print(" " * space2 , end = "")
#         c2 = inner
#         for k in range(1 , inner + 1):
#             print(c2 , end = "")
#             c2 -= 1
#         print()




sum = 1
for i in range(1, row + 1):
    for j in range(1, i + 1):
        print(sum, end=" ")
        sum += 1
    print()

# Lower half
for i in range(row, 0, -1):
    start = (i * (i - 1)) // 2 + 1
    end = start + i

    for j in range(start, end):
        print(j, end=" ")
    print()