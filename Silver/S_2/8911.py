import sys
input = sys.stdin.readline

dir=[(0,1),(1,0),(0,-1),(-1,0)]#시계방향
dirn=[0,1,2,3]

num = int(input())

for _ in range(num):
    s=input().strip()
    maxx=0
    maxy=0
    minx=0
    miny=0
    x=0
    y=0
    d=0
    
    for i in list(s):
        if i=="F":
            x+=dir[d][0]
            y+=dir[d][1]
            if x>maxx:
                maxx=x
            if x<minx:
                minx=x
            if y>maxy:
                maxy=y
            if y<miny:
                miny=y
        elif i=="B":
            x-=dir[d][0]
            y-=dir[d][1]
            if x>maxx:
                maxx=x
            if x<minx:
                minx=x
            if y>maxy:
                maxy=y
            if y<miny:
                miny=y
        elif i=="L":
            d=dirn[d-1]
        elif i=="R":
            d=dirn[d-3]
            
    print((maxx-minx)*(maxy-miny))