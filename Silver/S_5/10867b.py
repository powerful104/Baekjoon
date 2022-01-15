#파이썬 전용
s=set()
int(input())

s=set(list(map(int, input().split())))
sli=list(s)
sli.sort()
print(" ".join(map(str,sli)))
