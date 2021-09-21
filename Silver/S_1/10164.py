from math import factorial as f
a,b,c= map(int, input().split())
if c==0:
    print(f(a+b-2) // (f(a-1) * f(b-1)))
else:
    x=(c-1)//b+1
    y=(c-1)%b+1
    print((f(x+y-2) // (f(x-1) * f(y-1)))*(f(a-x+b-y) // (f(a-x) * f(b-y))))