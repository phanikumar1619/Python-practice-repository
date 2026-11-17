def number_generator():
    a = int(input("Enter ending number:"))
    for i in range(1 , a+1):
        yield i

gen = number_generator()
# print(next(gen))

for i in gen:
    print(i)