s= input()
s = s.replace('()','a')
cur=0
ans=0

for i in list(s):
    if i=='a':
        ans+=cur
    elif i=='(':
        cur+=1
        ans+=1
    else:
        cur-=1
print(ans)