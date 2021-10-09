from itertools import permutations as pe
li=list(pe(list(range(1,int(input())+1))))
for i in li:
    print(" ".join(map(str,i)))