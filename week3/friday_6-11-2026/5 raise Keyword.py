age = input("Enter the age: ")

try:
    age = int(age)
    if(age >= 18):
        print("Eligible")
    else:
        raise ValueError("age is lessthan 18 so your not eligible")
except ValueError as e:
    print(e)