char = str(input("Enter the character of what you want: "))
if(char.isupper()):
    print("the character was capitial letter")
elif(char.islower()):
    print("the character was small letter")
elif(char.isdigit()):
    print("the character was digit")
else:
    print("the character was special character")