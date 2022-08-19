N = int(input())
nums = list(map(int, input().split()))

buf = [0]*4000001

for num in nums:
    buf[num] += 1

for i in range(-2000000, 2000001):
    for j in range(buf[i]):
        print(i, end=" ")
print()
