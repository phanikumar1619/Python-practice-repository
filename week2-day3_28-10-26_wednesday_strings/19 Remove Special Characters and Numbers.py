text = input("Enter a string: ")
result = ""

for ch in text:
    if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
        result += ch

print("Original string:", text)
print("After removing special characters and numbers:", result)