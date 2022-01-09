from math import gcd as g

a,b= map(int, input().split())
c,d= map(int, input().split())
e=a*d+c*b
f=b*d

print(e//g(e,f),f//g(e,f))
