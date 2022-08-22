N = int(input())

dic = {'TTT' : 0, 'TTH' : 1, 'THT' : 2, 'THH' : 3, 
       'HTT' : 4, 'HTH' : 5, 'HHT' : 6, 'HHH' : 7, }

for _ in range(N):
    s = input()
    ans = [0] * 8
    
    for i in range(38):
        ans[dic[s[i:i+3]]] += 1
            
    print(" ".join(list(map(str, ans))))