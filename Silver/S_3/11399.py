num = int(input())
li = list(map(int, input().split()))
li.sort()
ans=0
for i in range(len(li)):
    ans+=sum(li[:i+1])
print(ans)