scores = []

for i in range(5):
    scores.append([sum(list(map(int,input().split()))), i])

scores.sort()

print(scores[-1][1] + 1, scores[-1][0])