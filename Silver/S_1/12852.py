N = int(input())

dp =[[0, []] for _ in range(N)]
dp[0][1].append(1)

for i in range(2, N + 1):
    
    tmp_min = 100
    
    if i % 3 == 0:
        tmp_min = dp[i//3 - 1][0]
        dp[i-1][0] = dp[i//3 - 1][0] + 1
        dp[i-1][1] = [i] + dp[i//3 - 1][1]
    if i % 2 == 0 and tmp_min > dp[i//2 - 1][0]:
        tmp_min = dp[i//2 - 1][0]
        dp[i-1][0] = dp[i//2 - 1][0] + 1
        dp[i-1][1] = [i] + dp[i//2 - 1][1]
    if tmp_min > dp[i - 2][0]:
        tmp_min = dp[i - 2][0]
        dp[i-1][0] = dp[i - 2][0] + 1
        dp[i-1][1] = [i] + dp[i - 2][1]

print(dp[N-1][0])
print(' '.join(map(str,dp[N-1][1])))