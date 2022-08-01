N, K = map(int, input().split())
ans = 0
while True:
    if bin(N + ans)[2:].count('1') <= K:
        break
    ans += 1

print(ans)