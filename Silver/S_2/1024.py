N, L = map(int, input().split())

for i in range(L, 102):
    seq_sum = sum(list(range(i)))
    if seq_sum > N or i == 101:
        print(-1)
        break
    org = N - seq_sum
    if org % i == 0:
        for j in range(i):
            print((org // i) + j, end = ' ')
        break
