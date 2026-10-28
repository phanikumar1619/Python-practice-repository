n = input("Enter the n vaule: ")

big = 0
for i in range(0 , len(n)-1):
    if(n[i] < n[i+1]):
        big = n[i+1]
    else:
        big = n[i]
print("The big digit in a number: ",big)