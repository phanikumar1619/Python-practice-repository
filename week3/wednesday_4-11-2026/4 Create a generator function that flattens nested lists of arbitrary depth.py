
nested_list = [1, [2, 3], [4, [5, 6]], 7]

def num(my_list):
    for i in my_list:
        if isinstance(i, list):
            yield from num(i)
        else:
            yield i

gen = num(nested_list)

for i in gen:
    print(i)
