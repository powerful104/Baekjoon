def rect(n):
    if n == 1:
        return [["*"]]
    ret = [[] for _ in range(n)]
    prev = rect(n//3)
    
    for i in range(3):
        for j in range(n//3):
            if i == 1:
                ret[j+(n//3)*i] = (prev[j] + [" "]*(n//3) + prev[j])
            else:
                ret[j+(n//3)*i] = (prev[j]*3)
                
    return ret

n = int(input())

for i in rect(n):
    print("".join(i))

"""
나는 문제를 보니 재귀를 떠올렸는데
어떤 사람은 반복문으로 먼저 정사각형을 별로 다 채우고 나서 수를 줄여가며 큰사각형 부터 공백으로 바꾸는 방법을 사용하였다.

n=int(input())
s='*'
while n>1:
 t=[i*3 for i in s]
 s=t+[i+' '*len(i)+i for i in s]+t
 n//=3
print('\n'.join(s))
"""