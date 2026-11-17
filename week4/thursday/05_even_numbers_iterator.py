class EvenNumbers:

    def __init__(self , start , end):
        self.start = start
        self.end = end
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        while(self.start <= self.end):
            if(self.start % 2 == 0):
                val = self.start
                self.start += 1
                return val
            self.start += 1
        raise StopIteration

a = int(input("Starting number:"))
b = int(input("Ending number:"))
print("Even Numbers:")
obj = EvenNumbers(a , b)
for i in obj:
    print(i)
