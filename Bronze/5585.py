N = 1000 - int(input())
ans = 0
coins = [500,100,50,10,5,1]

for coin in coins:
    ans += N//coin
    N %= coin

print(ans)