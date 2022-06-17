n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))
coins.sort()

dp = [1] + [0] * k

for coin in coins:
    for i in range(coin, k+1):
        dp[i] += dp[i-coin]

print(dp[k])