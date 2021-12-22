a,b= map(int, input().split())
m = int(input())
li = list(map(int, input().split()))
li.reverse()
num=0
ra=1

for i in li:
    num+=i*ra
    ra*=a
lit=[]

while num!=0:
    lit.append(num%b)
    num=num//b
lit.reverse()
print(" ".join(map(str,lit)))
