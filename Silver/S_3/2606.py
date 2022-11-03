import sys
sys.setrecursionlimit(10000000)

N = int(input())
M = int(input())

con_map = [[] for _ in range(N)]
visited = set()

for _ in range(M):
    a, b = map(int,input().split())
    con_map[a-1].append(b-1)
    con_map[b-1].append(a-1)

def dfs(to):
    if to in visited:
        return
    
    visited.add(to)
    
    for i in con_map[to]:
        dfs(i)

dfs(0)

print(len(visited)-1)