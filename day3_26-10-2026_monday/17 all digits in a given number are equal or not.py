n = input("Enter the number :")
count = 0

for i in range( 0 , len(n)-1):
    if(int(n[i]) == int(n[i+1])):
        count += 1

if(count > 0):
    print("All digits are equal.")
else:
  print("All digits are not equal.")