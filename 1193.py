import re

N = int(input())
nums = list(filter(None, re.split(r'[a-zA-Z]',input())))

ans = 0

for num in map(int,nums):
    if num < 1000000:
        ans += num

print(ans)