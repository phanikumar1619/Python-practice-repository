def find_second_smallest(numbers):

    large = numbers[0]
    for i in numbers:
        if large < i:
            large = i
    second_large = None
    for i in numbers:
        if large > i:
            if second_large is None or second_large < i :
                second_large = i

    print("Second lagest number:",second_large)




numbers = [10, 50, 30, 80, 20]

a = find_second_smallest(numbers)