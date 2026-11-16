class EvenNumbers:

    def __init__(self , start , end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if(self.start >= 0):
            if(self.start % 2 == 0):
                val = self.start
                return val
            else:
                self.start += 1
        else:
            raise StopIteration

a = int(input("Starting number:"))
b = int(input("Ending number:"))
print("Even Numbers:")
stop = 0
obj = EvenNumbers(a , b)
for i in obj:
    if(stop == b):
        break
    else:
        print(i)
        stop += 1
