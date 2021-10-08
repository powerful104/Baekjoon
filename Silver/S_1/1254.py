def palin(s):
    ans = 1
    for i in range(len(s) // 2):
        if s[i] != s[-(1 + i)]:
            ans = 0
    return ans
s=input()
for i in range(len(s)):
    se=s[i:]
    if palin(se)==1:
        break
print(len(s)+i)