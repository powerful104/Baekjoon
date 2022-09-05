import sys
input = sys.stdin.readline

N = int(input())

max_dp = [0, 0, 0]
min_dp = [0, 0, 0]

for _ in range(N):
    nums = list(map(int, input().split()))
    tmp_dp = [0, 0, 0]
    
    for i in range(3):
        tmp_dp[i] = max(max_dp[max(0,i-1):min(3,i+2)]) + nums[i]
    max_dp = list(tmp_dp)

    for i in range(3):
        tmp_dp[i] = min(min_dp[max(0,i-1):min(3,i+2)]) + nums[i]
    min_dp = list(tmp_dp)

print(max(max_dp), min(min_dp))