def pibo():
    pibos = [0, 1]
    while True:
        tmp = pibos[-1] + pibos[-2]
        pibos.append(tmp)
        if tmp > 1000000000:
            break
    return pibos

pibos = pibo()

T = int(input())
for _ in range(T):
    N = int(input())
    ans = []
    while(N != 0):
        for i in range(len(pibos)):
            if pibos[i] > N:
                N -= pibos[i-1]
                ans.append(pibos[i-1])
                break
    print(" ".join(map(str,reversed(ans))))
