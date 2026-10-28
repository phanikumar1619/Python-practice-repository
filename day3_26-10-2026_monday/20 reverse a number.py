n = input("Enter the n value: ")

# print(n[::-1])

full = len(n)
for i in range(full - 1 , -1 , -1):
    print(n[i], end = "\n")