import sys
input = sys.stdin.readline
a,b,c= map(int, input().split())
li=[]
sumli=[]

for _ in range(a):
    li.append(list(map(int, input().split())))
    
for i in range(a):
    lit=[]
    sum=0
    for j in range(b):
        sum+=li[i][j]
        lit.append(sum)
    sumli.append(list(lit))
    
for _ in range(c):
    r1, c1, r2, c2 = map(int, input().split())
    sum=0
    for i in range(r1-1,r2):
        sum+=sumli[i][c2-1]
        if c1>1:
            sum-=sumli[i][c1-2]
    print(sum//((r2-r1+1)*(c2-c1+1)))