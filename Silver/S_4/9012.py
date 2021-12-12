num = int(input())
for _ in range(num):
    s=str(input())
    ans=0
    check=0
    
    for i in range(len(s)):
        if s[i]=="(":
            ans+=1
        elif s[i]==")":
            ans-=1
        if ans<0:
            check=1
            break
    if ans>0 or check==1:
        print("NO")
    else:
        print("YES")