from math import factorial
n, k = map(int, input().split())

n-=1
k-=1

print(int(factorial(n)/(factorial(k)*factorial(n-k))))