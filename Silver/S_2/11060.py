N = int(input())
nums = list(map(int,input().split()))
nums.reverse()
dp = [0] + [-1 for _ in range(N-1)]

for i in range(1, N):
    min_ = 10001
    for j in range(max(0,i-nums[i]),i):
        if dp[j] != -1 and dp[j] + 1 < min_:
            min_ = dp[j] + 1
    if min_ == 10001:
        min_ = -1
    dp[i] = min_

print(dp[N-1])