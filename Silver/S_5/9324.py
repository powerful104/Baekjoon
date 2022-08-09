T = int(input())

for _ in range(T):
    s = input()
    
    dic = dict()
    
    check = 0
    for i in range(len(s)):
        c = s[i]
        
        if check == 1:
            check = 0
            continue
        
        if c not in dic:
            dic[c] = 1
        else:
            dic[c] += 1
            if dic[c] == 3:
                if i == len(s)-1 or s[i+1] != c:
                    print("FAKE")
                    break
                else:
                    dic[c] = 0
                    check = 1
    else:
        print("OK")