N = int(input())
nums = list(map(int,input().split()))

dp = [[1,1] for _ in range(N)]

ans = 1

for i in range(1,N):
    if nums[i-1] <= nums[i]:
        dp[i][0] = dp[i-1][0] + 1
    
    if nums[i-1] >= nums[i]:
        dp[i][1] = dp[i-1][1] + 1

    ans = max(ans,max(dp[i]))

print(ans)