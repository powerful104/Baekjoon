import itertools as ite

while True:
    li = list(map(int, input().split()))
    if li[0]==0:
        break
    num=li[0]
    del li[0]
    lit = ite.combinations(li,6)
    for i in lit:
        print(" ".join(map(str,i)))
    print()
