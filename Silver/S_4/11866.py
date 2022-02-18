n, k = map(int, input().split())
a = list(range(1,n+1))
ans= []
num=0

for i in range(0,n):
    num += k-1
    if num >= len(a):
        num = num%len(a)
    ans.append(a.pop(num))
print("<", end="")

for i in range(0, n):
    print(ans[i], end="")
    if (i != n - 1):
        print(", ", end="")
print(">")