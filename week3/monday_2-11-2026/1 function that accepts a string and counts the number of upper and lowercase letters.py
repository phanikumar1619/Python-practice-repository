def findupper(text):
    count = 0
    for i in range(len(text)):
        if(text[i].isupper()):
            count += 1
    return count

def findlower(text):
    count = 0
    for i in range(len(text)):
        if(text[i].islower()):
            count += 1
    return count

text = input("Enter the string value :")

uper = findupper(text)
loer = findlower(text)

print("No. of uppercase characters:",uper)
print("No. of Lower-case Characters:",loer)