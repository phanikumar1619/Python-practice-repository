year = int(input("Enter the birth year "))

age = 0

if(year < 2026):
    for i in range(2026):
        if(year == 2026):
            break
        age = age + 1
        year = year + 1
    print("Your age is:",age)
else:
    print("Enter the correct birth year")