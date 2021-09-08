from math import factorial as f
a,b= map(int, input().split())
print(f(a+b-1)//(f(a)*f(b-1))%1000000000)