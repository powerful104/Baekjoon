N = int(input())
stairs = [0,0,0]
for _ in range(N):
    stairs.append(int(input()))

dp = [0] * (N + 3)

for i in range(3,N+3):
    dp[i] = stairs[i] + max(dp[i-2], stairs[i-1]+dp[i-3])

print(dp[-1])