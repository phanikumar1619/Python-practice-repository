text = input("Enter string :")

Alphabet = 0
vowels = 0
consonants = 0
spchar = 0
num = 0
words = 0

seen = ['a' , 'e' , 'i', 'o' ,'u']

for i in text:
    if(i.lower() in seen):
        vowels += 1 
    if(i.isalpha()):
        Alphabet += 1
    if not i.isalnum() and not i.isspace():
        spchar += 1
    if(i.isdigit()):
        num += 1

for i in range(len(text)):
    if text[i] != ' ' and (i == 0 or text[i-1] == ' '):
        words += 1

consonants = Alphabet - vowels


print("Alphabet:",Alphabet)
print("numbers:",num)
print("special character:",spchar)
print("vowels:",vowels)
print("consonants",consonants)
print("no of words:", words)

# words was not working properly i will look after