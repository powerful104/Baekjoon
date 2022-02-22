a, b = map(int, input().split())
li=[]
ans=1

for _ in range(a):
    li.append(str(input()))
    
for i in range(min(a,b)):
    check=0
    for j in range(a-i):
        for k in range(b-i):
            if li[j][k]==li[j+i][k]==li[j][k+i]==li[j+i][k+i]:
                check=1
                ans=i+1
                break
        if check==1:
            break
print(ans*ans)