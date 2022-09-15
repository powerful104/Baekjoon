import heapq

N = int(input())
heap = []

for i in range(N):
    for item in list(map(int,input().split())):
        heapq.heappush(heap, item)
        if i > 0:
            heapq.heappop(heap)

print(heap[0])