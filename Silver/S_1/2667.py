N = int(input())

map_ = []

for _ in range(N):
    map_.append(list(map(int, list(input()))))

def dfs(y, x):
    if x<= -1 or x >= N or y <= -1 or y >= N:
        return 0
    if map_[y][x] == 1:
        map_[y][x] = 0
        sum_ret = 1
        sum_ret += dfs(y-1, x)
        sum_ret += dfs(y, x-1)
        sum_ret += dfs(y+1, x)
        sum_ret += dfs(y, x+1)
        return sum_ret
    return 0

res = []
for i in range(N):
    for j in range(N):
        ans = dfs(i,j)
        if ans != 0:
            res.append(ans)

print(len(res))
for item in sorted(res):
    print(item)