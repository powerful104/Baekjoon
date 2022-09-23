import heapq
import sys
input = sys.stdin.readline

N = int(input())

heap = []

for _ in range(N):
    heapq.heappush(heap, int(input()))

ans = 0

while True:
    num1 = heapq.heappop(heap)
    
    if len(heap) == 0:
        break
    
    num2 = heapq.heappop(heap)
    ans += num1 + num2
    heapq.heappush(heap, num1 + num2)

print(ans)