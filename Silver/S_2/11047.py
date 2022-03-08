n, k= map(int, input().split())
li=[]
mod=k
ans=0

for _ in range(n):
    li.append(int(input()))
li.sort(reverse=True)

for i in li:
    ans+=mod//i
    mod=mod%i
print(ans)
