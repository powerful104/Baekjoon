T = int(input())

for _ in range(T):
    N = int(input())
    ans = set(map(int,input().split()))
    M = int(input())
    for i in list(map(int,input().split())):
        if i in ans:
            print(1)
        else:
            print(0)