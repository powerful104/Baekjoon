import re
s = input()
num = list(map(int, re.split('[-+]',s)))
exp = ' '.join(re.split('[0123456789]',s)).split()
cur = 0

while cur != len(exp):
    if exp[cur] == '+':
        num[cur:cur+2] = [num[cur]+num[cur+1]]
        exp[cur:cur+1] = []
    else:
        cur += 1
        
print(num[0]-sum(num[1:]))