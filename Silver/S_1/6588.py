import math

def is_prime_number(n):
    array = [True for i in range(n+1)]
    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1
    return array

prime = is_prime_number(1000000)
while True:
    n = int(input())
    if n == 0 :
        break
    i = 3
    j = n-3
    
    while True:
        if i > j:
            break
        if prime[i] and prime[j]:
            print(str(n)+" = "+str(i)+" + "+str(j))
            break
        i += 1
        j -= 1

"""
에라토스테네스의 체를 이용하여 소수에대한 참 거짓 리스트를 뽑아내고
해당 리스트를 이용하여 i를 점점 증가시켜가며 해당 i와 n-i가 둘다 소수를 만족하는지 확인한다.
"""
