import sys
input = sys.stdin.readline

li=[0]*1000

maxa=0
mina=1000
maxh=0
num = int(input())
for _ in range(num):
    a, b = map(int, input().split())
    li[a-1] = b
    if a>maxa:
        maxa=a
    if a<mina:
        mina=a
    if b>maxh:
        maxh=b
ans=0
for j in range(1,maxh+1):
    maxb=0
    minb=maxa
    for i in range(mina-1,maxa):
        if li[i]>=j:
            if i>maxb:
                maxb=i
            if i<minb:
                minb=i
    ans+=maxb-minb+1
print(ans)