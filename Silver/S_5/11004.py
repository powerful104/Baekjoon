import sys
a,b= map(int, input().split())
li = list(map(int, sys.stdin.readline().split()))
li.sort()
print(li[b-1])