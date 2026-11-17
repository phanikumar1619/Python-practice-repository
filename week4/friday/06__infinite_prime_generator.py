def prime():
    ending = int(input("How many prime numbers do you want?"))
    i = 2
    prime = 0
    while(prime < ending):
        count = 1
        for j in range(2 , i):
            if(i%j == 0):
                count += 1
        if count == 1:
            prime += 1
            yield i
        i += 1

gen = prime()

for i in gen:
    print(i)