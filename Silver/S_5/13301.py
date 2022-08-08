N = int(input())

def pibo(N):
    pibos = [1, 1]
    for i in range(2,N):
        pibos.append(pibos[i-1] + pibos[i-2])
    return pibos

pibos = pibo(N)

dp = [4] + [0]*(N-1)

for i in range(1,N):
    dp[i] = dp[i-1] + 2*pibos[i]

print(dp[N-1])