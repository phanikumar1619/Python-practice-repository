class Fibonacci:

    def __init__(self , number):
        self.number = number
        self.a = 0 
        self.b = 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):

        if(self.count == self.number):
            raise StopIteration

        else:
            re = self.a
            val = self.a + self.b
            self.a = self.b
            self.b = val
            self.count += 1
            return re

a = Fibonacci(5)
for i in a:
    print(i)
