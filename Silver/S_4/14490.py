import math as m
li = list(map(int, input().strip().split(":")))
g = m.gcd(li[0],li[1])
print(str(li[0]//g)+":"+str(li[1]//g))