T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    ans = 0
    for i in range(N, M+1):
        ans += list(str(i)).count('0')
    print(ans)