def prime_numbers():
    n = 2
    while True:
        count = 0
        for i in range(2 , n):
            if(n%i == 0):
                count += 1
        if(count == 0):
            yield n
        n += 1

a = prime_numbers()

for i in a:
    print(i)