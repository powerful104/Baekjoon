import math as m
num = int(input())

for _ in range(num):
    li = list(map(int, input().split()))
    ans=0
    
    for i in range(1,len(li)-1):
        
        for j in range(i+1,len(li)):
            ans+=m.gcd(li[i],li[j])
    print(ans)