n = input("Enter the n value: ")

odd = 0
even = 0
sum = 0
full = len(n)


for i in range(0 , full):
    if(i%2 == 0):
        even += int(n[i])
    else:
        odd += int(n[i])
    # print(int(n[i]))

sum = odd + even

print("Sum of even digits:",even)
print("Sum of odd digits:",odd)

print("Sum of even and odd digits:",sum)