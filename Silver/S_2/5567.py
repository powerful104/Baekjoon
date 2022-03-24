num = int(input())
numa = int(input())
sa=set()
sf=set()
li=[]

for _ in range(numa):
    a, b = map(int, input().split())
    li.append([min(a,b),max(a,b)])

li.sort()
check=0

for i in li:
    if i[0]!=1:
        break
    sa.add(i[1])
    sf.add(i[1])
    check+=1

for i in range(check,len(li)):
    if li[i][0] in sa:
        sf.add(li[i][1])
    if li[i][1] in sa:
        sf.add(li[i][0])
print(len(sf))