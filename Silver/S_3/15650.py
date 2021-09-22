import itertools as ite
a,b= map(int, input().split())
li = list(ite.combinations(range(1,a+1),b))
for i in li:
    print(" ".join(map(str,i)))