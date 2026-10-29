n = int(input("Enter the N value: "))

for i in range(0 , n+1):
    for j in range(1 , i+1):
        print(i, end = " ")
        i -= 1
    print("\n")
