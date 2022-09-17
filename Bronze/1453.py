N = int(input())
custs = list(map(int, input().split()))
use = []
ans = 0

for i in custs:
    if i in use:
        ans += 1
    else:
        use.append(i)

print(ans)