import math
a,b= map(int, input().split())
ans=0
z=math.floor(100*b/a)
low, high = 0, 1000000000

if z>=99:
    ans=-1
else:
    while low <= high:
        mid = (low + high) // 2
        ta, tb = a + mid, b + mid
        if math.floor(100 * tb / ta) > z:
            high = mid - 1
        else:
            low = mid + 1
    ans=high+1
    
print(ans)