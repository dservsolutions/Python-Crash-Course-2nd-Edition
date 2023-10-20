# 4.3 Counting to Twenty
for number in range(1, 21):
    print(number)
# numbers = [number for number in range(1, 21)]
# print(numbers)

# 4.4 One Million
one_million = []
# for value in range(1, 999999):
#     one_million.append(value)
# print(one_million)

# 4.5 Summing a Million
numbers = [value for value in range(1, 999999)]
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# 4.6 Odd numbers
odd = []
for values in range(1, 20, 2):
    odd.append(values)
print(odd)

# 4.7 Threes
result = []
for values in range(3, 31, 3):
    result.append(values)
print(result)

# multiples = [value**3 for value in range(3, 31, 3)]
# print(multiples)

# 4.8 Cubes
cubes = []
for values in range(1, 10):
    cubes.append(values**2)
print(cubes)

# 4.9 Cube comprehensions
cube = [value**2 for value in range(1, 10)]
print(cube)