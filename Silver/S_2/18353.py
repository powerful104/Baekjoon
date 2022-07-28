N = int(input())
soldiers = list(map(int, input().split()))
dp = [1] * N

for i in range(N):
    for j in range(i):
        if soldiers[i] < soldiers[j]:
            dp[i] = max(dp[j] + 1, dp[i])

print(N - max(dp))