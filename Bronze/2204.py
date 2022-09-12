while True:
    N = int(input())
    if N == 0:
        break
    li = []
    for _ in range(N):
        word = input()
        li.append([word.upper(), word])
    li.sort()
    print(li[0][1])