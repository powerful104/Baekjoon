a,b= map(int, input().split())
ans=0
check=0
while b>a:
    if str(b)[-1]=='1':
        b=b//10
    elif b%2==1:
        break
    else:
        b=b//2
    ans+=1
    if b==a:
        check=1
        break
if check==1:
    print(ans+1)
else:
    print(-1)