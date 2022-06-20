points = []

for i in range(1,9):
    points.append([int(input()), i])
points.sort(reverse = True)
last = 0

for point in points[:5]:
    last += point[0]
print(last)
numbers = []

for point in points[:5]:
    numbers.append(point[1])
numbers.sort()
print(' '.join(map(str, numbers)))