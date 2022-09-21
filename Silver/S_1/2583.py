import sys
sys.setrecursionlimit(10000000)

M, N, K = map(int,input().split())

map_ = [[0 for _ in range(N)] for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int,input().split())

    for y in range(y1,y2):
        for x in range(x1,x2):
            map_[y][x] = 1

def DFS(y, x):
    if (x < 0 or x >= N) or (y < 0 or y >= M):
        return 0
    
    if map_[y][x] == 0:
        ret = 1
        map_[y][x] = 1
        ret += DFS(y-1,x)
        ret += DFS(y,x-1)
        ret += DFS(y+1,x)
        ret += DFS(y,x+1)
        return ret
    else:
        return 0

nums = 0
area = []

for i in range(M):
    for j in range(N):
        res = DFS(i,j)
        if res != 0:
            nums += 1
            area.append(res)

print(nums)
print(' '.join(list(map(str, sorted(area)))))