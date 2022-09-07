N = int(input())

dp = [0] * (31)

dp[2] = 1

for i in range(2, N + 1):
    if i % 2 == 1:
        continue
    
    dp[i] += 2
    
    for j in range(i-2,0,-2):
        if j == i-2:
            dp[i] += dp[j]*3
        else:
            dp[i] += dp[j]*2

print(dp[N])