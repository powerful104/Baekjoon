n, d = map(int, input().split())

ans = 0

for i in range(1, n+1):
    ans += list(str(i)).count(str(d))

print(ans)