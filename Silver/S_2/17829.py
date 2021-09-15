li=[]
n=int(input())
for _ in range(n):
    li+=list(map(int, input().split()))
while n!=1:
    litmp=[]
    for j in range(0,n,2):
        for i in range(0,n,2):
            lic=[li[i+j*n],li[i+j*n+1],li[i+j*n+n],li[i+j*n+n+1]]
            lic.sort()
            litmp.append(lic[2])
    li=list(litmp)
    n=n//2
print(li[0])