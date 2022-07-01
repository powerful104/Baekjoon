N, M = map(int,input().split())
list_A = list(map(int,input().split()))
list_B = list(map(int,input().split()))

print(' '.join(list(map(str,sorted(list_A + list_B)))))