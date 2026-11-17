class EvenLinesIterator:
    def __init__(self , filename):
        self.filename = filename
        self.file = open(self.filename , "r")
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            val = self.file.readline()

            if val == "":
                self.file.close()
                raise StopIteration

            self.count += 1

            if self.count % 2 == 0:
                return val
            

a = EvenLinesIterator("students.txt")
for i in a:
    print(i , end = "")