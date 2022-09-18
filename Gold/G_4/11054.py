N = int(input())
nums = list(map(int,input().split()))
dp = [[1,1] for _ in range(N)]

ans = 0

for i in range(N):
    for j in range(i):
        if nums[i] > nums[j]:
            if dp[i][0] <= dp[j][0]:
                dp[i][0] = dp[j][0] + 1
        if nums[i] < nums[j]:
            if dp[j][1] < dp[j][0]:
                dp[j][1] = dp[j][0]
            if dp[i][1] <= dp[j][1]:
                dp[i][1] = dp[j][1] + 1
    if ans < max(dp[i]):
        ans = max(dp[i])

print(ans)