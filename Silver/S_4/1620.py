import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dic = dict()

for i in range(N):
    name = input().strip()
    dic[str(i+1)] = name
    dic[name] = str(i+1)

for _ in range(M):
    name = input().strip()
    print(dic[name])