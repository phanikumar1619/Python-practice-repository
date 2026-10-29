n = int(input("Enter the N value: "))

count = 1

for i in range(0 , n+1):
    for j in range(1 , i+1):
        print(count, end = " ")
        count += 1
    print("\n")