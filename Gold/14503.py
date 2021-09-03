import copy
n, m= map(int, input().split())
r, c, d= map(int, input().split())

ve=[0,1,2,3]
vec=[(-1,0),(0,1),(1,0),(0,-1)]
_map=[]
_maptest=[]
ans=0
anst=0
for _ in range(n):
    li=[]
    li=list(map(int, input().split()))
    _map.append(list(li))
for i in _map:
    ans+=i.count(1)
_maptest=copy.deepcopy(_map)
_map[r][c]=1
while True:
    if _map[r-1][c]+_map[r][c+1]+_map[r+1][c]+_map[r][c-1]>3:
        rt=r+vec[d-2][0]
        ct=c+vec[d-2][1]
        if _maptest[rt][ct]!=0:
            break
        else:
            r+=vec[d-2][0]
            c+=vec[d-2][1]
    else:
        rt=r+vec[d-1][0]
        ct=c+vec[d-1][1]
        if _map[rt][ct]==0:
            d=ve[d-1]
            r+=vec[d][0]
            c+=vec[d][1]
            _map[r][c]=1
        else:
            d=ve[d-1]
for i in _map:
    anst+=i.count(1)

print(anst-ans)