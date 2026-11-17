start = int(input("Enter the number"))
stop = int(input("Enter the number"))
count = 0

# while(count < stop):
#     if(start % 2 == 0):
#         print(start)
#         start += 1
#         count += 1
#     else:
#         start += 1

for i in range(start , stop+1):
    if(i % 2 == 0):
        print(i)