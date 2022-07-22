import sys
sys.setrecursionlimit(10**6)

M, N= map(int, input().split())

graph = []

for _ in range(M):
    graph.append(list(map(int,input().split())))

def dfs(x, y):
    if x<= -1 or x >= M or y <= -1 or y >= N:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        
        dfs(x-1, y)
        dfs(x-1, y-1)
        dfs(x, y-1)
        dfs(x-1, y+1)
        dfs(x+1, y)
        dfs(x+1, y-1)
        dfs(x, y+1)
        dfs(x+1, y+1)
        return True
    return False

result = 0
for i in range(M):
    for j in range(N):
        if dfs(i, j) == True:
            result += 1

print(result)