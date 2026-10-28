def dig(n):
    sum = 0 
    rem = 0
    while(n > 0):
        # for i in range(1 , n):
        rem = n % 10
        sum = sum + rem
        n = n // 10
    print(sum)

n = int(input("enter the n value: "))
dig(n)