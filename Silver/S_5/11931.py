import sys
input = sys.stdin.readline

N = int(input())

sor = [0] * 2000002

for _ in range(N):
    sor[int(input())] = 1

for i in range(1000000,-1000001,-1):
    if sor[i] == 1:
        print(i)