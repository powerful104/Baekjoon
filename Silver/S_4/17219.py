import sys
input = sys.stdin.readline
N, M = map(int,input().split())
pw_book = dict()

for _ in range(N):
    cite, pw = input().split()
    pw_book[cite] = pw

for _ in range(M):
    cite = input().strip()
    print(pw_book[cite])
    
    """
    처음에 너무 복잡하게 생각하고 풀었는데
    파이썬의 딕셔너리형을 이용하면 간단한 문제였다.
    """