def unpack_tuple(n):
    name , age , lan , marks = n[0] , n[1] , n[2] , n[3]
    print("Name:", name)
    print("Age:", age)
    print("Course:" , lan)
    print("Marks:" , marks)



tup = ("Phani", 22, "Python", 90)
a = unpack_tuple(tup)