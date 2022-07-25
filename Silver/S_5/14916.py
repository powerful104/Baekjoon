N = int(input())
coins = [2, 5]
dp = [0] + [-1] * (N)

for i in range(1, N + 1):
    
    mn_ = 100000
    for coin in coins:
        if i-coin >= 0 and dp[i-coin] < mn_ and dp[i-coin] != -1:
            mn_ = dp[i-coin]
    if mn_ != 100000:
        dp[i] = mn_ + 1
        
print(dp[N])