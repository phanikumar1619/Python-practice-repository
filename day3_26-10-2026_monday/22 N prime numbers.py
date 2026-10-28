n = int(input("Enter the N value: "))

prim = 0
i = 2

while(prim < n):
    count = 0
    for j in range(2 , i):
        if(i%j == 0):
            count += 1
    if(count == 0):
        prim += 1
        print(i)
    i += 1