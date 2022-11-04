import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline


N, M = map(int, input().split())

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

ans = 0

for i in range(N):
    if i in visited:
        continue
    dfs(i)
    ans += 1

print(ans)