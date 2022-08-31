from itertools import product
import itertools
N, M = map(int,input().split())
nums = list(map(int, input().split()))
nums.sort()

data = itertools.product(nums, repeat=M)

for i in data:
    print(' '.join(list(map(str,list(i)))))