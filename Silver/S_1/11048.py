a,b= map(int, input().split())
li=[]
for _ in range(a):
    li.append(list(map(int, input().split())))
for i in range(a):
    for j in range(b):
        if i==0:
            if j!=0:
                li[i][j]+=li[i][j-1]
        else:
            if j!=0:
                li[i][j]+=max(li[i][j-1],li[i-1][j])
            else:
                li[i][j]+=li[i-1][j]
print(li[a-1][b-1])