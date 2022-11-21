N, L = map(int,input().split())
nums = list(map(int,input().split()))

nums.sort()

for i in nums:
    if i <= L:
        L += 1

print(L)