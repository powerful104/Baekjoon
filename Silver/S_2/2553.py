N = int(input())

fact = 1

for i in range(1,N+1):
    fact *= i
    
    fact %= 10000000
    while(fact % 10 == 0):
        fact //= 10

print(fact % 10)