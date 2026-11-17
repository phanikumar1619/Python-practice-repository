num = int(input("Enter ending number:"))

gen = (i*i for i in range(1 , num+1))

for i in gen:
    print(i)