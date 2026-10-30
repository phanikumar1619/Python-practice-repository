text = input("Enter the text :")

worlds = text.split()

pt = []

print(worlds)

for i in worlds:
    a = ord(i[0]) - 1
    b = chr(a)
    c = i[1:]
    pt.append(b+c)

print(pt)