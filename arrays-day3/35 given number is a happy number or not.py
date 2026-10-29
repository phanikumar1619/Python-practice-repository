n = int(input("Enter the N value: "))

seen = set()

while n != 1 and n not in seen:
    seen.add(n)
    total = 0

    while n > 0:
        digit = n % 10
        total = total + digit ** 2
        n = n // 10

    n = total

if n == 1:
    print("It is a Happy Number")
else:
    print("It is not a Happy Number")