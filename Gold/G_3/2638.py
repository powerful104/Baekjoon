import sys
sys.setrecursionlimit(10000000)

N, M = map(int, input().split())

cheese_map = []
new_cheese_map = []
air_map = [[1 for _ in range(M)] for _ in range(N)]

dir = ((0,1), (1,0), (0,-1), (-1, 0))

for _ in range(N):
    cheese_map.append(list(map(int,input().split())))

def air_DFS(y, x):
    if (x < 0 or x >= M) or (y < 0 or y >= N):
        return False
    
    if cheese_map[y][x] == 0 and air_map[y][x] == 1:
        air_map[y][x] = 0
        air_DFS(y-1,x)
        air_DFS(y,x-1)
        air_DFS(y+1,x)
        air_DFS(y,x+1)
        return True
    return False

air_DFS(0, 0)

ans = 0

while True:
    tmp_sum = 0
    
    for i in range(N):
        tmp_sum += sum(cheese_map[i])
    
    if tmp_sum == 0:
        break
    
    air_map = [[1 for _ in range(M)] for _ in range(N)]
    air_DFS(0, 0)
    
    new_cheese_map = list(cheese_map)
    
    for y_ in range(N):
        for x_ in range(M):
            if cheese_map[y_][x_] != 1:
                continue
            check = 0
            for d in dir:
                if air_map[y_ + d[0]][x_ + d[1]] == 0:
                    check += 1
            if check >= 2:
                new_cheese_map[y_][x_] = 0
    
    cheese_map = list(new_cheese_map)
    
    ans += 1

print(ans)