import sys
a,b= map(int, input().split())
list=[]

for _ in range(a):
    list.append(float(sys.stdin.readline()))
list.sort()

for _ in range(b):
    del list[0]
    list.pop()
    
print("{:.2f}".format(round(sum(list)/len(list)+0.00000001,2)))
list+=[list[0]]*b+[list[len(list)-1]]*b
print("{:.2f}".format(round(sum(list)/len(list)+0.00000001,2)))