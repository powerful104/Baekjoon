s = input()

LArr = []
answer = False

for j in s:
    if len(LArr) != 0 and ((LArr[-1] == '(' and j == ')')):
        LArr.pop()
    else:
        LArr.append(j)

if len(LArr) == 0:
    answer = True

"""

"""