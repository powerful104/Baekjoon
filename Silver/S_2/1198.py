N = int(input())
points = []

def getArea(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return abs(x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3)/2

for _ in range(N):
    points.append(list(map(int,input().split())))

max_ = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            area = getArea(points[i], points[j], points[k])
            if area > max_:
                max_ = area
print(max_)