from itertools import product

N, M = map(int, input().split())
numbers = sorted(list(set(list(map(int, input().split())))))

for i in product(numbers, repeat = M):
    print(' '.join(map(str, list(i))))