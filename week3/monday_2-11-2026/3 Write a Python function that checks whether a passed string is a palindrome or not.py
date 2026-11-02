def palindrome(n):
    text = n[:: -1]
    if(n == text):
        return True
    else:
        return False


n = input("Enter the N value :")

des = palindrome(n)

if(des == True):
    print("It is a Palindrome")
else:
    print("It is not a Palindrome")