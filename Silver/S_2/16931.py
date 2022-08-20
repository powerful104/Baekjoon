N, M = map(int,input().split())

blocks = []

blocks.append([0]*(M+2))
for _ in range(N):
    blocks.append([0] + list(map(int,input().split())) + [0])
blocks.append([0]*(M+2))

ans = N*M*2

for i in range(N+1):
    for j in range(M+1):
        ans += max(blocks[i][j],blocks[i+1][j]) - min(blocks[i][j],blocks[i+1][j])
        ans += max(blocks[i][j],blocks[i][j+1]) - min(blocks[i][j],blocks[i][j+1])

print(ans)