import sys
sys.setrecursionlimit(10000000)

M, N = map(int,input().split())

map_ =[]

for _ in range(M):
    map_.append(list(map(int, list(input()))))

def DFS(y, x):
    if (x < 0 or x >= N) or (y < 0 or y >= M):
        return
    
    if map_[y][x] == 0:
        map_[y][x] = 2
        DFS(y-1,x)
        DFS(y,x-1)
        DFS(y+1,x)
        DFS(y,x+1)

for i in range(N):
    DFS(0,i)

if 2 in map_[M-1]:
    print('YES')
else:
    print('NO')