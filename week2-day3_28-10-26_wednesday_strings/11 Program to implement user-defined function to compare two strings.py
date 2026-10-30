def compare(text1 , text2):
    if(text1 == text2):
        print("Both strings are equal.")
    else:
        print("Both strings are not equal.")


text1 = input("Enter the first string: ")
text2 = input("Enter the second string: ")

compare(text1 , text2 )


'''
same using for loops

python
def compare(text1, text2):

    if len(text1) != len(text2):
        print("Both strings are not equal.")
        return

    for i in range(len(text1)):
        if text1[i] != text2[i]:
            print("Both strings are not equal.")
            return

    print("Both strings are equal.")


text1 = input("Enter the first string: ")
text2 = input("Enter the second string: ")

compare(text1, text2)
'''