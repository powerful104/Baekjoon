import sys
input = sys.stdin.readline

N = int(input())

players = dict()

for _ in range(N):
    name = input()
    if players.get(name) == None:
        players[name] = 1
    else:
        players[name] += 1

for _ in range(N-1):
    name = input()
    players[name] -= 1

for key in players.keys():
    if players[key] == 1:
        print(key)
        break