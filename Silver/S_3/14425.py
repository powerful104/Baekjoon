N, M = map(int, input().split())

words = set()
ans = 0

for _ in range(N):
    words.add(input())
for _ in range(M):
    if input() in words:
        ans += 1

print(ans)