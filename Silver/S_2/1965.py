N = int(input())
nums = list(map(int, input().split()))
dp = [1] * N

for i in range(N):
    mx = 0
    for j in range(0,i):
        if nums[i] > nums[j] and dp[j] > mx:
            mx = dp[j]
    dp[i] = mx + 1

print(max(dp))