import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    A, B = map(int, input().split())
    print(A + B)