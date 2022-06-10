N = int(input())
slimes = sorted(list(map(int, input().split())))

score = 0

for i in range(N-1):
    score += slimes[i] * slimes[i+1]
    slimes[i+1] += slimes[i]

print(score)