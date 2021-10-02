import itertools as it
num = int(input())
li = list(map(int, input().split()))
result = list(it.permutations(li,num))
max=0
for j in result:
    ans=0
    for i in range(num-1):
        ans+=abs(j[i]-j[i+1])
    if max<ans:
        max=ans
print(max)