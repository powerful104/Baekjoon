import heapq
import sys
heap = []
input = sys.stdin.readline

for _ in range(int(input())):
    x = int(input())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap,(-1*x,x))


"""
sys를 사용하지 않고 input을 사용했더니 시간이 초과되길래 sys를 사용하여 입력 시간을 줄였다.
"""