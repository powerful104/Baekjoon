import sys
num = int(input())
li=[]
mi=list(range(1,num+1))
si=set()
ans=[]
check=0
siold=0
sinew=0
silen=0
big=0
for _ in range(num):
    li.append(int(sys.stdin.readline()))
for i in li:
    if i>big:
        siold=len(si)
        si.update(list(range(big+1,i+1)))
        sinew=len(si)
        silen=sinew-siold
        big=i
        ans+=["+"]*silen
    if i != max(si):
        print("NO")
        check=1
        break
    si.remove(i)
    ans+=["-"]
if check==0:
    for i in ans:
        print(i)