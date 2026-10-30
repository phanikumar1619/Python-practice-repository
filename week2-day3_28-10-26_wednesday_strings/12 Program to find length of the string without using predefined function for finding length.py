def size(text1):
    length = 0
    for i in text1:
        length += 1
    return length

text1 = input("Enter the String: ")

print("Length of the string:",size(text1))
