def solution(s, n):
    answer = [s//n]*n
    s = s % n
    for i in range(s):
        answer[-1*(i+1)] += 1
    if answer.count(0) > 0:
        return [-1]
    return answer

def multiply(arr):
    ans = 1
    for n in arr:
        if n == 0:
            return 0
        ans *= n
    return ans

S, K = map(int, input().split())
print(multiply(solution(S, K)))
