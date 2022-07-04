n, k = map(int, input().split())

dp = [[[]]] + [[] for _ in range(n)]

for i in range(1, n+1):
    for j in [1,2,3]:
        if i >= j:
            for dps in dp[i-j]:
                dp[i].append(dps + [j])
        else:
            break
    dp[i].sort()

if k > len(dp[n]):
    print(-1)
else:
    print('+'.join(list(map(str,dp[n][k-1]))))