import heapq

T = int(input())

for _ in range(T):
    M = int(input())
    
    lheap = []
    rheap = []
    nums = []
    for _ in range((M-1)//10 + 1):
        nums += list(map(int, input().split()))
    mid = nums[0]
    print((M+1)//2)
    print(mid, end = " ")
    for i in range(1,len(nums)):
        if i % 20 == 0:
            print()
        
        if i % 2 == 0:
            if nums[i] < mid:
                heapq.heappush(lheap,-1*nums[i])
                heapq.heappush(rheap, mid)
                mid = -1*heapq.heappop(lheap)
            else:
                heapq.heappush(rheap, nums[i])
            print(mid, end = " ")
        else:
            if nums[i] < mid:
                heapq.heappush(lheap, -1*nums[i])
            else:
                heapq.heappush(rheap, nums[i])
                heapq.heappush(lheap, -1*mid)
                mid = heapq.heappop(rheap)
    print()
