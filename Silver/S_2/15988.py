import sys
input = sys.stdin.readline

N = int(input())

dp = [1] + [0]*(1000000)

for i in range(1, 1000000 + 1):
    for j in range(1, min(i, 3) + 1):
        dp[i] += dp[i-j]
    dp[i] = dp[i]%1000000009

for _ in range(N):
    num = int(input())
    print(dp[num])
    
    """
    두가지 버전으로 풀어봤는데 위의 버전이 더 짧고 시간도 절약되는것 같다.
    
    import sys
    input = sys.stdin.readline

    N = int(input())

    dp = [1] + [0]*(1000000)

    for _ in range(N):
        num = int(input())
        if dp[num] == 0:
            for i in range(1, num + 1):
                if(dp[i] != 0):
                    continue
                for j in range(1, min(i, 3) + 1):
                    dp[i] += dp[i-j]
                dp[i] = dp[i]%1000000009
        print(dp[num])
    
    """