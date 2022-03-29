N, r, c= map(int, input().split())
li=[]

for i in range(N-1,-1,-1):
    if r>2**i-1:
        if c>2**i-1:
            li.append(3)
            c=c-2**i
        else:
            li.append(2)
        r=r-2**i
    else:
        if c>2**i-1:
            li.append(1)
            c=c-2**i
        else:
            li.append(0)
            
ans=0
r=1
li.reverse()

for i in range(len(li)):
    ans+=li[i]*r
    r*=4
    
print(ans)
