N = int(input())

dp =["CY"] + ["" for _ in range(N+5)]

for i in range(N):
    if dp[i] == "SK":
        s = "CY"
    else:
        s = "SK"
    for num in [1,3,4]:
        if dp[i+num] == "":
            dp[i+num] = s

print(dp[N])