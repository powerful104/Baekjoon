a,b= map(int, input().split())
li=list(range(2,a+1))
mi=0
ans=0

while True:
    c=min(li)
    mi+=1
    check=0
    
    if mi==b:
        ans=c
        break
    del li[0]
    
    for i in li:
        if i%c==0:
            del li[li.index(i)]
            mi += 1
            if mi == b:
                ans = i
                check=1
                break
            
    if check==1:
        break
print(ans)
