N = input()
ans = set()

for i in range(1,len(N)+1):
    for j in range(0,len(N)-i+1):
        ans.add(N[j:j+i])

print(len(ans))