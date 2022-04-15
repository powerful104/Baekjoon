def fibo(n):
    fn = 0
    fn1 = 1
    ans = fn1
    
    for _ in range(n - 1):
        ans = fn + fn1
        fn = fn1
        fn1 = ans
    return ans

num = int(input())

for _ in range(num):
    n = int(input())
    if(n==0):
        print(1,0)
    elif(n==1):
        print(0,1)
    else:
        print(fibo(n-1),fibo(n))