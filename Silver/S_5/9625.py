def BABBA(N):
    A = 1
    B = 0
    new_A = 0
    new_B = 0
    for _ in range(N):
        new_A = B
        new_B = A + B
        
        A = new_A
        B = new_B
    print(A, B)

BABBA(int(input()))

"""
해당 BABBA 함수는 결국 피보나치와 같다.
"""