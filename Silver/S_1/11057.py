from math import factorial as f
num = int(input())
print(f(num+9)//(f(9)*f(num))%10007)