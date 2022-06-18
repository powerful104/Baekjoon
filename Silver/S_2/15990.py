import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    dp = [[[1],[1],[1]]] + [[0],[0],[0]] * n
    for i in range(1, 4):
        for j in range(i,n+1):
            dp[j] += dp[j-i]
            dp[j] %= 1000000009
    print(dp[n])
    