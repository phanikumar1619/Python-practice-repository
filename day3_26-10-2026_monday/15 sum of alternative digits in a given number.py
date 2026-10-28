n = input("Enter the n value: ")

sum = 0
for i in range(0 , len(n) , 2):
    sum += int(n[i])
    # print(int(n[i]))

print(sum)