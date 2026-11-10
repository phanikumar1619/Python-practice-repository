text = input("Enter a string: ")

ascending = sorted(text, key=str.lower)
descending = sorted(text, key=str.lower, reverse=True)

print("Alphabetical order:", "".join(ascending))
print("Reverse alphabetical order:", "".join(descending))