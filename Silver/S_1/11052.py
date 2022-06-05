N = int(input())
P = list(map(int, input().split()))

dp = [0] * (N + 1 + len(P))

for i in range(1, N + 1):
    for j in range(min(i, len(P))):
        dp[i] = max(dp[i], dp[i-j-1] + P[j])

print(dp[N])