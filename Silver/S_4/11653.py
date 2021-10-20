num = int(input())
n = 1
while True:
    n+=1
    if num==1:
        break
    if num%n==0:
        print(n)
        num=num//n
        n=1