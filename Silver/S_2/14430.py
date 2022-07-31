N, M = map(int, input().split())
gather_map = []

for _ in range(N):
    gather_map.append(list(map(int, input().split())))

dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,M+1):
        dp[i][j] = max(dp[i-1][j],dp[i][j-1]) + gather_map[i-1][j-1]

print(dp[N][M])