row = int(input("Enter the rows values:"))

# count = 1
# for i in range(1 , row + 1):
#     for j in range(1 , i + 1):
#         print(count, end = " ")
#         count += 1
#     print()



step = 1
for i in range(1 , row + 1):
    for j in range(step , row):
        print(j , end = "")
    for k in range(1 , i):
        print(k , end = "")
    step += 1
    print()


# text = "fzaektavzvnyvngaqbenadebh"
# text2 = ""
# for i in range(-1 , -len(text)-1 , -1):
#     text2 += text[i]

# print(text2)

# len = 0

# for i in text:
#     len += 1

# print("lenght" , len)