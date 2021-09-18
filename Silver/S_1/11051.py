import math as m
a,b= map(int, input().split())
print(m.factorial(a)//(m.factorial(b)*m.factorial(a-b))%10007)