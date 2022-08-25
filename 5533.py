N = int(input())

players = []
times = [[],[],[]]

for _ in range(N):
    player = list(map(int, input().split()))
    players.append(player)
    for i in range(3):
        times[i].append(player[i])

for i in range(N):
    for j in range(3):
        if players[i][j] in times[j] and times[j].count(players[i][j]) != 1:
            players[i][j] = 0
    print(sum(players[i]))