import math as m
while True:
    num = int(input())
    if num==0:
        break
    print(m.factorial(2*num)//(m.factorial(num)*m.factorial(num)*(num+1)))