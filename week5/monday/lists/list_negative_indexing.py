numbers = [15, 25, 35, 45, 55, 65, 75]

n = len(numbers)

print("First Element: ", numbers[0])
print("First Element: ", numbers[-n])
print("Last Element: ", numbers[n-1])
print("Last Element: ", numbers[-1])
print("Second From End:" , numbers[-2])
print("Third From End:" , numbers[-3])
mid = int(n/2) + 1
print("Middle Element:" , numbers[-mid])
numbers[-2] = 100
print("Updated List:",numbers)