def Pn(num):
    n1=1
    n2=1
    n3=1
    n4=2
    n5=2
    if num==1 or num==2 or num==3:
        return 1
    elif num==4 or num==5:
        return 2
    else:
        for _ in range(num-5):
            n6=n5+n1
            n1=n2
            n2=n3
            n3=n4
            n4=n5
            n5=n6
        return n6

num = int(input())
for _ in range(num):
    print(Pn(int(input())))