def fibo(n):
    fn1 = 1
    fn2 = 1
    fn3 = 1
    if n==1 or n==2 or n==3:
        ans=1
    else:
        for _ in range(3,n):
            ans = fn1 + fn3
            fn1 = fn2
            fn2 = fn3
            fn3 = ans
    return ans
print(fibo(int(input())))