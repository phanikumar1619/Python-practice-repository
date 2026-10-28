n = input("Enter the number :")
a = int(input("Enter a digit to find :"))
count = 0

for i in range(0 , len(n)):
    if(int(n[i]) == a):
        count += 1
        # print(int(n[i]))

print("The digit {} occurs {} times.".format(a,count))