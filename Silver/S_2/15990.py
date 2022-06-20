import sys
input = sys.stdin.readline

T = int(input())
max_li = 3
dp = [[1,0,0],[0,1,0],[1,1,1]] + [[0,0,0] for _ in range(100000-3)]

for i in range(3, 100000):
    for j in range(1, 4):
        dp[i][j-1] = sum(dp[i-j]) - dp[i-j][j-1]
        dp[i][j-1] %= 1000000009

for _ in range(T):
    n = int(input())
    print(sum(dp[n-1])%1000000009)