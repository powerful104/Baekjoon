n, k = map(int, input().split())
coins = []
dp = [0] + [1000000 for _ in range(k)]

for _ in range(n):
    coins.append(int(input()))

coins = sorted(list(set(coins)))

for coin in coins:
    for i in range(coin, k+1):
        if dp[i] > dp[i-coin]:
            dp[i] = dp[i-coin] + 1

if dp[k] == 1000000:
    print(-1)
else:
    print(dp[k])