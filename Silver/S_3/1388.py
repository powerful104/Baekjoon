N, M = map(int, input().split())

fl = []

for _ in range(N):
    fl.append(list(input()))

ans = 0

for i in range(N):
    for j in range(M):
        if fl[i][j] == '-':
            if j == 0 or (j != 0 and fl[i][j-1] != '-'):
                ans += 1
        else:
            if i == 0 or (i != 0 and fl[i-1][j] != '|'):
                ans += 1

print(ans)