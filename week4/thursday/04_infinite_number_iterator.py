# class InfiniteNumbers:

#     def __init__(self , start , end):
#         self.start = start
#         self.end = end

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if(self.start >= 0 and self.start <= self.end):
#             val = self.start
#             self.start += 1
#             return val
#         else:
#             raise StopIteration

# a = int(input("Starting number:"))
# b = int(input("Number of values to display:"))
# print("Infinite Number Sequence:")
# obj = InfiniteNumbers(a , b)
# for i in obj:
#     print(i)



class InfiniteNumbers:

    def __init__(self , start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if(self.start >= 0):
            val = self.start
            self.start += 1
            return val

a = int(input("Starting number:"))
count = int(input("Number of values to display:"))
print("Infinite Number Sequence:")
stop = 0
obj = InfiniteNumbers(a)
for i in obj:
    if(stop == count):
        break
    else:
        print(i)
        stop += 1
