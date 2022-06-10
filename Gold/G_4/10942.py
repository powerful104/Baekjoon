import sys
input = sys.stdin.readline

N = int(input())
num_List = list(map(int, input().split()))
M = int(input())

dp = [[0] * (N + 1) for _ in range(N + 1)]

for E in range(1,N+1):
    for S in range(1,E+1):
        if E-S <= 1:
            if num_List[E-1] == num_List[S-1]:
                dp[S][E] = 1
        else:
            if dp[S+1][E-1] == 1 and num_List[E-1] == num_List[S-1]:
                dp[S][E] = 1
            else:
                dp[S][E] = 0
                
for _ in range(M):
    S, E = map(int, input().split())
    print(dp[S][E])