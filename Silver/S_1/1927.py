import heapq
import sys
heap = []
input = sys.stdin.readline
N = int(input())

for _ in range(N):
    x = int(input())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap,x)

"""
sys를 사용하지 않고 input을 사용했더니 시간이 초과되길래 sys를 사용하여 입력 시간을 줄였다.
"""
