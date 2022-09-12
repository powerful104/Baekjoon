N = int(input())

ans = 0

for i in range(1,N):
    ans += i + i*N

print(ans)