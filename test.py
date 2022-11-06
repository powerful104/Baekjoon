from math import inf

def solution(worldmap):
    answer = 0
    dp_map = [[[inf,inf,inf] for _ in range(len(worldmap[0]))] for _ in range(len(worldmap))]
    dp_map[0][0] = [0,0,0]
    N = len(worldmap)
    M = len(worldmap[0])
    for y in range(1, N):
        for x in range(1, M):
            if worldmap[y][x] == 'X':
                continue
            if x-1 >= 0:
                dp_map[y][x][0] = min(dp_map[y][x-1][0],dp_map[y][x-1][2])+1
            if y-1 >= 0:
                dp_map[y][x][1] = min(dp_map[y-1][x][1],dp_map[y-1][x][2])+1
            if x-1 >= 0 and y-1 >= 0:
                if worldmap[y-1][x] != 'X' and worldmap[y][x-1] != 'X':
                    dp_map[y][x][2] = min(dp_map[y-1][x-1])+1
    answer = min(dp_map[N-1][M-1])
    return answer

print(solution(["..XXXXX","...XXXX",".......","......."]))