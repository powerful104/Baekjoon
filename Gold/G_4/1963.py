from collections import deque

def prime_list(n):
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True]

def change_poss(num1, num2):
    check = 0
    for i in range(4):
        if str(num1)[i] == str(num2)[i]:
            check += 1
    
    if check == 3:
        return True
    else:
        return False

li = prime_list(10001)[168:]

nums_dic = {}
graph = [[] for _ in range(len(li))]

def bfs(start, goal, visited):
    queue = deque([nums_dic[start]])
    visited[nums_dic[start]] = 1
    
    if start == goal:
        print(0)
        return
    
    ans = 1
    while queue:
        tmpq = deque()
        for v in queue:
            for i in graph[v]:
                if visited[i] != 1:
                    if li[i] == goal:
                        print(ans)
                        return
                    tmpq.append(i)
                    visited[i] = 1
        queue = tmpq
        ans += 1

for i in range(len(li)):
    nums_dic[li[i]] = i
    for j in range(len(li)):
        if change_poss(li[i], li[j]):
            graph[i].append(j)

for _ in range(int(input())):
    visi = [0 for _ in range(1061)]
    num1, num2 = map(int, input().split())
    bfs(num1, num2, visi)