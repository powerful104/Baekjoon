n, m = map(int, input().split())
 
data = []
 
for i in range(n):
    s = input()
    data.append(list(map(int, list(s))))
 
dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
side = 0
 
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if data[i - 1][j - 1] == 1:
            dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
 
            if dp[i][j] > side:
                side = dp[i][j]
 
print(side**2)