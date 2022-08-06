T = int(input())

def is_palin(str1, str2):
    str3 = str1 + str2
    return str3 == str3[::-1]

for _ in range(T):
    N = int(input())
    words = []
    
    for _ in range(N):
        words.append(input())
    
    chk = 0
    
    for i in range(N-1):
        for j in range(i+1, N):
            if is_palin(words[i], words[j]):
                print(words[i]+words[j])
                chk = 1
                break
            elif is_palin(words[j], words[i]):
                print(words[j]+words[i])
                chk = 1
                break
        if chk == 1:
            break
    else:
        print(0)