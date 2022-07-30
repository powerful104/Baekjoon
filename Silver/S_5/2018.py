N = int(input())

num = 0
ans = 0

for i in range(1, N+1):
    num += i
    if num > N:
        break
    if (N - num) % i == 0:
       ans += 1
       
print(ans)