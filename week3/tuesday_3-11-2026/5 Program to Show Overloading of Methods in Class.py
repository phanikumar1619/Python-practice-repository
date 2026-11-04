class Add:
    def add_numbers(self , a , b , c = 0):
        total = a+ b + c
        print("the sum of numbers are :",total)

a = Add()
a.add_numbers(4 , 5)
a.add_numbers(4 , 6 , 5)