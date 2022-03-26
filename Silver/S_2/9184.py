import sys
input = sys.stdin.readline

li = [[[0 for x in range(21)] for y in range(21)] for z in range(21)]

for i in range(21):
    for j in range(21):
        li[0][i][j]=1
        li[i][0][j]=1
        li[i][j][0]=1
        
for i in range(1,21):
    for j in range(1,21):
        for k in range(1,21):
            if i<j<k:
                li[i][j][k] = li[i][j][k-1] + li[i][j-1][k-1] - li[i][j-1][k]
            else:
                li[i][j][k] = li[i-1][j][k] + li[i-1][j-1][k] + li[i-1][j][k-1] - li[i-1][j-1][k-1]
                
while True:
    a, b, c = map(int, input().split())
    oa=int(a)
    ob=int(b)
    oc=int(c)
    if a==b==c==-1:
        break
    if a<=0 or b<=0 or c<=0:
        a=0
        b=0
        c=0
    elif a>20 or b>20 or c>20:
        a=20
        b=20
        c=20
    print("w("+str(oa)+", "+str(ob)+", "+str(oc)+") = "+str(li[a][b][c]))