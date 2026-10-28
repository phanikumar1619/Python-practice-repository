n = int(input("Enter the N value: "))

per = 0
i = 1

while(per < n):
    sum = 0
    for j in range(1 , i):
        if(i%j == 0):
            sum += j
    if(sum == i):
        per += 1
        print("the perfect number is :",i)
    i += 1