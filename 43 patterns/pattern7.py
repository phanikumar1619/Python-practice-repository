n = int(input("Enter the N value: "))


for i in range(0 , n+1):
    count = n
    for j in range(1 , i+1):
        print(count, end = " ")
        count -= 1
    print("\n")