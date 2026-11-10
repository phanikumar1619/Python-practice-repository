#names = ["Phani", "Pavan", "Rahul", "Praveen", "Ravi", "Kiran"]

names = input("Enter names separated by spaces: ")
names_list = names.split()


letter = input("Enter starting character: ")

print("Names starting with", letter, ":")

for name in names_list:
    if name.lower().startswith(letter.lower()):
        print(name)