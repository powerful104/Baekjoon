N = int(input())

# 0은 빈 상태, 1은 왼쪽, 2는 오른쪽

fence = [[1, 1, 1]] + [[0,0,0] for _ in range(N - 1) ]

for i in range(1,N):
    fence[i][0] += (fence[i-1][0] + fence[i-1][1] + fence[i-1][1]) % 9901
    fence[i][1] += (fence[i-1][0] + fence[i-1][2]) % 9901
    fence[i][2] += (fence[i-1][0] + fence[i-1][1]) % 9901

print(sum(fence[N-1]) % 9901)

"""
(1+x)/(1-2*x-x^2)
다음 수식으로 나타낼수도있다.
"""