def chk(x,b):
    s=[]
    while x>0:
        s.insert(0,x%b)
        x=x//b
    return s

def is_palin(str_):
    return str_ == str_[::-1]

T = int(input())

for _ in range(T):
    N = int(input())
    for B in range(2, 65):
        if is_palin(chk(N,B)):
            print(1)
            break
    else:
        print(0)