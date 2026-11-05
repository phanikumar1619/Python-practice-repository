class Number:
    def __init__(self , n):
        self.n = n

    def Fibonacci(self):
        a = 0
        b = 1
        # print(a,end = ",")
        # print(b,end = ",")
        n = self.n
        yield a
        yield b
        while True:
            c = a + b

            if c > n:
                break

            print(c, end = ",")
            a = b
            b = c
a = Number(50)
gen = a.Fibonacci()

for i in gen:
    print(i, end = ",")