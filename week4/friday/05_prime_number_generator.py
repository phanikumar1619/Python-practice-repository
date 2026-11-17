def prime():
    ending = int(input("Enter ending number:"))

    for i in range(2 , ending + 1):
        count = 1
        for j in range(2 , i):
            if(i%j == 0):
                count += 1
        if count == 1:
            yield i

gen = prime()

for i in gen:
    print(i)