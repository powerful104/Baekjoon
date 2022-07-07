from cv2 import split


T = int(input())

for _ in range(T):
    n = int(input())
    
    dic = dict()
    
    answer = 1
    for _ in range(n):
        fash, typ = input().split()
        if typ not in dic.keys():
            dic[typ] = 1
        else:
            dic[typ] += 1
    for _, i in dic.items():
        answer *= (i+1)
    answer -= 1
    
    print(answer)