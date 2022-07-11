import sys
input = sys.stdin.readline

s = input()

dp = [[0 for _ in range(26)] for _ in range(len(s) + 1)]

for i in range(len(s)):
    ind = ord(s[i])-ord('a')
    for j in range(26):
        if j == ind:
            dp[i][j] = dp[i-1][j] + 1
        else:
            dp[i][j] = dp[i-1][j]

T = int(input())
for _ in range(T):
    c, start, end = input().split()
    ind = ord(c)-ord('a')
    print(dp[int(end)][ind]-dp[int(start)-1][ind])