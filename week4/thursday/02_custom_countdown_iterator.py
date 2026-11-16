class Countdown:

    def __init__(self , start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if(self.start == 0):
            print("Countdown completed!")
            raise StopIteration
        else:
            val = self.start
            self.start -= 1
            return val

a = Countdown(5)
print("Countdown:")
for i in a:
    print(i)