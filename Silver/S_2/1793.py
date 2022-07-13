dp = [1,1] + [0 for _ in range(250-1)]

for i in range(2, 250+1):
    dp[i] = dp[i-1] + dp[i-2]*2

while True:
    try: n = int(input())
    except: break
    print(dp[n])