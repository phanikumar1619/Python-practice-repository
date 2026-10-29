str = input("Enter the String :")

for i in range(len(str)-1 , -1 , -1):
    print(str[i],end = ",")

print(str[ :: -1])

t = 0 
for i in str:
    t += 1

print(t)

p = len(str)
print(p)