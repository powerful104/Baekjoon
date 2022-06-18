N = int(input())
home = []
for _ in range(N):
    home.append(list(map(int, input().split())))

directions = ((-1, -1), (-1, 0), (0, -1))
dp = [[0] * N for _ in range(N)]
dp[0][1] = 1
for i in range(N):
    for j in range(1,N):
        if home[i][j] != 1:
            for dir in directions:
                dir_i = i + dir[0]
                dir_j = j + dir[1]
                if not (dir_i < 0  or dir_j < 0):
                    print(dir_i,dir_j)
                    dp[i][j] += dp[dir_i][dir_j]

print(dp[N-1][N-1])