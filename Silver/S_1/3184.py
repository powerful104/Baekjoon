import sys
sys.setrecursionlimit(10000000)

R, C = map(int,input().split())

map = []
dirs = [(0,1),(1,0),(0,-1),(-1,0)]

for _ in range(R):
    map.append(list(input()))

def dfs(y, x):
    if (x < 0 or x >= C) or (y < 0 or y >= R) or (map[y][x] == '#'):
        return (0, 0)
    
    sheep = 0
    wolf = 0
    
    if map[y][x] =='o':
        sheep += 1
    elif map[y][x] == 'v':
        wolf += 1
    
    map[y][x] = '#'
    
    for dir in dirs:
        sh, w = dfs(y+dir[0], x+dir[1])
        sheep += sh
        wolf += w
    return (sheep, wolf)

sheep = 0
wolf = 0

for y in range(R):
    for x in range(C):
        sh, w = dfs(y, x)
        if sh > w:
            sheep += sh
        else:
            wolf += w

print(str(sheep) + " " + str(wolf))