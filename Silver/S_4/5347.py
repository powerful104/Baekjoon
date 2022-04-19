import math as m
num = int(input())

for _ in range(num):
    a,b= map(int, input().split())
    c = m.gcd(a,b)
    print(a//c*b)