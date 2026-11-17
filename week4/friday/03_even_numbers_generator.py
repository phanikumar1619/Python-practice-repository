def even_numbers_generator():
    start = int(input("Enter starting number:"))
    stop = int(input("Enter ending number:"))
    for i in range(start , stop + 1):
        if(i % 2 == 0):
            yield i

a = even_numbers_generator()
for i in a:
    print(i)