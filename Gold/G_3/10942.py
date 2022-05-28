N = int(input())
num_List = list(map(int, input().split()))
M = int(input())

dp = [[0] * (N + 1) for _ in range(N + 1)]

def is_palin(num_List):
    check = 1
    for i in range(len(num_List)):
        if num_List[i] != num_List[len(num_List)-1-i]:
            check = 0
    return check

for j in range(1,N+1):
    for i in range(j-1,N):
        if dp[j-1][i+1] == 0:
            dp[j][i] = is_palin(num_List[j-1:i+1])
        else:
            dp[j][i] = 1


for _ in range(M):
    S, E = map(int, input().split())
    print(dp[S][E-1])