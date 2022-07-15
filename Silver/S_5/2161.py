N = int(input())

nums = list(range(1, N+1))

for _ in range(N-1):
    print(nums[0],end = " ")
    nums = nums[2:] + [nums[1]]

print(nums[0])