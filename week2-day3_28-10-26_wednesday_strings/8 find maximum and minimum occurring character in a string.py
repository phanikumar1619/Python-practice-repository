str = input("Enter the String :")

coun = 0
c = []
seen = []
for i in str:
    if(i in seen):
        pass
    else:
        seen.append(i)

for i in seen:
    coun = str.count(i)
    c.append(coun)

large = c[0]
small = c[0]
siz = len(c)
ind1,ind2 = 0,0

for i in range(siz):
    if(small > c[i]):
        small = c[i]
        ind1 = i
    if(large < c[i]):
        large = c[i]
        ind2 = i

print("Maximum occurring character: {} ({} times)".format(seen[ind2] , large))
print("Minimum occurring character: {} ({} time)".format(seen[ind1] , small))    