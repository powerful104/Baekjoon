import math
N = int(input())
answer = 0
for k in range(1, N + 1):
    answer += k * math.floor(N/k)
print(answer)