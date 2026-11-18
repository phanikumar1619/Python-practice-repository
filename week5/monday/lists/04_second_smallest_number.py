def find_second_smallest(numbers):

    # small = numbers[0]
    # for i in numbers:
    #     if small > i:
    #         small = i
    second_small = None
    for i in numbers:
        if small < i:
            if second_small is None or second_small > i :
                second_small = i

    print("Second smallest number:",second_small)




numbers1 = [45, 12, 89, 7, 23, 56]
numbers = [1, 2, 3, 4, 5]
numbers2 = [8, 5, 2, 1, 9]

a = find_second_smallest(numbers1)
b = find_second_smallest(numbers)
c = find_second_smallest(numbers2)