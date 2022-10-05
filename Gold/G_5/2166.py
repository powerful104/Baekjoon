N = int(input())

points = []

for _ in range(N):
    points.append(tuple(map(int,input().split())))

ans = 0.0

for i in range(N):
    ans += points[i-1][0]*points[i][1]-points[i][0]*points[i-1][1]

ans = abs(ans)

ans /= 2

print(ans)