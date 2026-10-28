n = int(input("Enter the N value: "))


dig = 0

if(n < 0):
    n = -1 * n
if(n == 0):
    dig = 1

while(n > 0):
    dig += 1
    n = n//10
print(dig)