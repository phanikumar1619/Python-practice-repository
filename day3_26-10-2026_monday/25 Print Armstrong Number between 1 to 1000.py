# n = int(input("Enter the N value: "))


# dig = 0
# org = n

# if(n < 0):
#     n = -1 * n
# if(n == 0):
#     dig = 1

# while(org > 0):
#     dig += 1
#     org = org//10

# sum = 0
# for i in range(1, dig+1):
#     rem = n%10
#     sum = sum + pow(rem , dig)
#     n = n // 10

# if(sum == org):
#     print("yes")
# else:
#     print("no")


n = int(input("Enter the N value: "))

dig = 0
org = n

if n < 0:
    n = -n
    org = -org

temp = n

if n == 0:
    dig = 1

while temp > 0:
    dig += 1
    temp = temp // 10

temp = n
total = 0

for i in range(1, dig + 1):
    rem = temp % 10
    total = total + pow(rem, dig)
    temp = temp // 10

if total == n:
    print("yes")
else:
    print("no")