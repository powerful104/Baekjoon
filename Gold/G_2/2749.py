import math

def period(M):
    k = int(math.log10(M))
    return 15 * (10 ** (k-1))

N = int(input())

M = 1000000

P = period(M)

N %= P

fn1 = 0
fn2 = 1

for _ in range(N-1):
    fn1, fn2 = fn2 % M, (fn2+fn1) % M

print(fn2 % M)

"""
피사노 주기 이용 문제풀이
피보나치수는 나머지에 무조건 주기가 존재한다.
해당내용을 이용하여 문제풀이
"""