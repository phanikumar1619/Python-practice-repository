text = input("Enter the string: ")

upper = 0
lower = 0
vowels = 0
consonants = 0
digits = 0
special = 0
total = len(text)
seen = ['a' , 'e' , 'i', 'o' ,'u']

for i in range(len(text)):
    if(text[i].isupper()):
        upper += 1
    if(text[i].islower()):
        lower += 1
    if(text[i].isdigit()):
        digits += 1
    if not text[i].isalpha() and not text[i].isspace():
        special += 1
    if text[i].lower() in seen:
        vowels += 1
    if text[i].isalpha() and text[i].lower() not in seen:
        consonants += 1

print(vowels)
print(consonants)

def per(n , total):
    pr = (n/total)*100
    return pr

print("Upper:",per(upper , total))
print("lower:",per(lower , total))
print("vowels:",per(vowels , total))
print("consonants:",per(consonants , total))
print("digits:",per(digits , total))
print("special:",per(special , total))