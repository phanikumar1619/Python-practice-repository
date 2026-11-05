nested_list = [1, [2, 3], [4, [5, 6]], 7]

def num():
    for i in nested_list:
        if isinstance(i, list):
            yield num()
        else:
            yield i 

gen = num()

for i in gen:
    print(i)