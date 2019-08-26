numbers = list(range(3,31,3))
print(numbers)
for value in list(range(3,31,3)):
    print(value)
cubes = []
for value in range(1,11):
    cube = value**3
    cubes.append(cube)
print(cubes)    
cubes = []
for value in range(1,11):
    cubes.append(value**3)
print(cubes)
cubes = [value**3 for value in range(1,11)]
print(cubes)