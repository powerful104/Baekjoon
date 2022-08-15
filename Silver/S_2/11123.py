import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())

    graph = []
    for i in range(n):
        graph.append(list(input()))

    def dfs(x, y):
        if x<= -1 or x >= n or y <= -1 or y >= m:
            return False
        if graph[x][y] == '#':
            graph[x][y] = '.'
            
            dfs(x-1, y)
            dfs(x, y-1)
            dfs(x+1, y)
            dfs(x, y+1)
            return True
        return False

    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                result += 1

    print(result)