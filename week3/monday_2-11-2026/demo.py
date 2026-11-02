# print the prime number from 1 to n numbers
n = int(input("Enter the given number :"))

for i in range(2 , n+1):
    count = 0
    for j in range(2 , i+1):
        if(i%j == 0):
            count += 1
    if(count == 1):
        print(i)


# print string first words capitialized in the given string
text = input("Enter the text value :")
textor = ""
for i in range(0 , len(text)):
    if(i == 0 or text[i - 1] == ' '):
        textor = textor + text[i].upper()
    else:
        textor = textor + text[i]

print(textor)


#print the sum of odd and even numbers in the given number
n = int(input("Enter the value of N :"))
odd = 0
even = 0

while(n > 0):
    rem = n % 10
    if(rem%2 == 0):
        even = even + rem
    else:
        odd = odd + rem
    n = n // 10

print(odd)
print(even)