import sys
input = sys.stdin.readline

N = int(input())

sticks = []

for _ in range(N):
    sticks.append(int(input()))
sticks.reverse()

last = 0
ans = 0

for stick in sticks:
    if stick > last:
        ans += 1
        last = stick

print(ans)