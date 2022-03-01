import itertools as ite
a,b= map(int, input().split())
lit = list(map(int, input().split()))
lit.sort()
li = list(ite.combinations(lit,b))

for i in li:
    print(" ".join(map(str,i)))