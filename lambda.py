add = lambda x, y: x + y

print(add(5, 3))

numbers = [1, 2, 3, 4, 5, 6]
even_nums = list(filter(lambda x: x % 2 == 0, numbers))
print(even_nums)

cube_nums = list(map(lambda x: x**3, numbers))
print(cube_nums)


