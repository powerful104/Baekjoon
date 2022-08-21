import sys
input = sys.stdin.readline

while True:
    N, M = map(int, input().split())

    if N == 0 and M == 0:
        break
    
    sg = set([])
    sy = set([])

    for _ in range(N):
        sg.add(int(input()))
    for _ in range(M):
        sy.add(int(input()))

    print(len(sg.intersection(sy)))