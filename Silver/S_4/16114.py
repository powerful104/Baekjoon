a,b= map(int, input().split())
ans=""
if b%2!=0 and b!=1: #1 제외 홀수 거름
    ans="ERROR"
elif b==0 and a>0 or b==1 and a<0:
    ans="INFINITE"
elif a<=b//2 or b==1 and a>=0:
    ans="0"
elif a%(b//2)==0:
    ans=str(a//(b//2)-1)
else:
    ans=str(a//(b//2))
print(ans)