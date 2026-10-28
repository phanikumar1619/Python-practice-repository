# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# salary = int(input("Enter your salary: "))

# print("My name is: ",name)
# print("My age is: ",age)
# print("My salary is: ",salary)

# chocolates = 23
# friends = 4

# # Calculate chocolates per friend

# print("chocolates per friend: ",(chocolates // friends))

# # Calculate remaining chocolates

# print("remaining chocolates: ",chocolates%friends)


# numbers = [10, 20, 30 , 90 , 50]
# min = numbers[0]
# max = numbers[0]
# for i in range(len(numbers)):
#     if(min > numbers[i]):
#         min = numbers[i]
#     if(max < numbers[i]):
#         max = numbers[i]

# print(min)
# print(max)


numbers = [10, 20, 10, 30, 20, 40, 10]

cont = 0
for i in range(len(numbers)):
    if(numbers[i] == 10):
        cont = cont + 1
print(cont)