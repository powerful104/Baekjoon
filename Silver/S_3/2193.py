def pin(n):
    pn = 0
    pn1 = 1
    ans = pn1
    
    for _ in range(n - 1):
        ans = pn + pn1
        pn = pn1
        pn1 = ans
    return ans

num = int(input())
print(pin(num))