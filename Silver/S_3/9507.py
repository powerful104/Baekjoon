def fibo(n):
    fn = 0
    fn1 = 1
    fn2 = 1
    fn3 = 2
    if n==0 or n==1:
        ans=1
    elif n==2:
        ans=2
    else:
        for _ in range(2,n):
            ans = fn + fn1 + fn2 + fn3
            fn = fn1
            fn1 = fn2
            fn2 = fn3
            fn3 = ans
    return ans

tc = int(input())
for _ in range(tc):
    num = int(input())
    print(fibo(num))