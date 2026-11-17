class FileReader:

    def __init__(self, filename):
        self.filename = filename
        self.file = open(self.filename, "r")

    def __iter__(self):
        return self

    def __next__(self):
        val = self.file.readline()

        if val == "":
            self.file.close()
            raise StopIteration

        return val


a = FileReader("sample.txt")


for i in a:
    print(i, end="")