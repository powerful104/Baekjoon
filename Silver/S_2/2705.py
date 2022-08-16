T = int(input())

dp = [1] * 1001

for i in range(1,1001):
    for j in range(i-2,-1,-2):
        dp[i] += dp[(i-j)//2]

for _ in range(T):
    N = int(input())
    print(dp[N])