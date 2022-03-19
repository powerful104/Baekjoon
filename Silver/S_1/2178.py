def solution(maps):
    dir = [(1,0), (0,1), (-1,0), (0,-1)]

    #map 재구성
    x = len(maps[0])
    y = len(maps)
    for i in maps:
        i.insert(0,0)
        i.append(0)
    maps.insert(0,[0]*(x+2))
    maps.append([0]*(x+2))

    #BFS
    queue =[(1,1)]
    maps[1][1] = -1
    
    while len(queue) != 0:
        curX = queue[0][0]
        curY = queue[0][1]
        del queue[0]
        for i in dir:
            if maps[curY+i[1]][curX+i[0]] > 0:
                queue.append((curX+i[0],curY+i[1]))
                maps[curY+i[1]][curX+i[0]] = maps[curY][curX]-1
                
    if maps[y][x] > 0:
        answer = -1
    else:
        answer = -maps[y][x]
    return answer

a,b = map(int,input().split())
mp = []
for i in range(a):
    mp.append(list(map(int,input())))
print(solution(mp))

"""
프로그래머스의 게임 맵 최단 거리와 유사한 문제이다.
"""
