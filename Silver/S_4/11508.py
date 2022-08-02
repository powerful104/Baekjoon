import sys
input = sys.stdin.readline

N = int(input())

s_list = [0] * 100001

for _ in range(N):
    s_list[int(input())] += 1

prods = []

for i in range(100000,0,-1):
    for _ in range(s_list[i]):
        prods.append(i)

check = 0
ans = 0
for prod in prods:
    check += 1
    if check % 3 == 0:
        continue
    ans += prod

print(ans)