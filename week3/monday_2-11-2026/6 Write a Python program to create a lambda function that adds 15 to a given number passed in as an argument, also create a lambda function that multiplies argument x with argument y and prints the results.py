n = int(input("Enter a number :"))

x = int(input("Enter the value of x :"))

y = int(input("Enter the value of y :"))

add = lambda n : n + 15

mul = lambda x , y : x * y

print("After adding 15:",add(n))
print("After multiplication:",mul(x , y))