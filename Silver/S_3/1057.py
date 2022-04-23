a, b, c= map(int, input().split())
ans=0

if a<b or a<c:
    ans=-1
else:
    while b!=c:
        b = (b + 1) // 2
        c = (c + 1) // 2
        ans +=1
        
print(ans)