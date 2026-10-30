names = []

n = int(input("Enter the N vaule :"))


for i in range(n):
    val = input("Enter the value :")
    names.append(val)

ch  = input("Enter the character to find :")

for i in names:
    if(i[0] == ch):
        print(i)
    

# print(names)