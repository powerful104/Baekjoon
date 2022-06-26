import sys
input = sys.stdin.readline

N = int(input())

dp = [1] + [0 for _ in range(10000)]

for i in [1,2,3]:
    for j in range(i, 10000 + 1):
        dp[j] += dp[j-i]

for _ in range(N):
    T = int(input())
    print(dp[T])