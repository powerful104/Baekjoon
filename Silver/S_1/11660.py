import sys
input = sys.stdin.readline

N, M = map(int, input().split())

nums = []

for _ in range(N):
    nums.append(list(map(int, input().split())))

dp = [[0] * N for _ in range(N + 1)]

for i in range(N):
    for j in range(N):
        dp[i][j] = dp[i-1][j] + nums[i][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    up = 0
    down = 0
    for i in range(y1-1,y2):
        up += dp[x1-2][i]
        down += dp[x2-1][i]
    
    print(down - up)