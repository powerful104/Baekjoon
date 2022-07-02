import math as m

T = int(input())

for _ in range(T):
    N = int(input())
    N += 9
    print(int(m.factorial(N)/(m.factorial(N-9)*m.factorial(9))))