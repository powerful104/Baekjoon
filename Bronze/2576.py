nums = []

for _ in range(7):
    n = int(input())
    if n % 2 != 0:
        nums.append(n)
        
if len(nums) == 0:
    print(-1)
else:
    print(sum(nums))
    print(min(nums))