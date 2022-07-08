N = int(input())
sq_nums = [i**2 for i in range(1,int(N**0.5)+1)]

dp = [0] * (N + 1)

for i in range(1, N+1):
    min = 1000
    for sq_num in sq_nums:
        if sq_num > i:
            break
        if min > dp[i-sq_num]:
            min = dp[i-sq_num]
    dp[i] = min + 1

print(dp[N])