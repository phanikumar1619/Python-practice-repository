'''

Explanation Step by Step

Step 1: Create the generator function

def read_file(filename):


This function accepts the filename as an argument.

Example:
read_file("data.txt")


Step 2: Open the file
with open(filename, "r") as file:


- open() opens the file.
- "r" means read mode.
- with automatically closes the file after the block finishes.


Step 3: Read the file line by line

for line in file:


This is the important part.

Python reads the file one line at a time instead of loading all the lines into a list.

Step 4: Use yield
yield line.strip()


- yield returns one line at a time.
- strip() removes the newline character \n and surrounding whitespace.
- The generator pauses after yielding each line.
Step 5: Call the generator
e.txgen = read_file("data.txt")


This creates a generator object.

The file-reading code does not begin executing immediately. It begins when you request values from the generator.
Step 6: Iterate through the generator
for line in gen:    print(line)


Python requests each line from the generator and prints it.

'''



def read_file(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line.strip()


gen = read_file("email.txt")

for line in gen:
    print(line)