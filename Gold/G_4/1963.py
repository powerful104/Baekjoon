def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우 
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]

def change_poss(num1, num2):
    check = 0
    for i in range(4):
        if str(num1)[i] == str(num2)[i]:
            check += 1
    
    if check == 1:
        return True
    else:
        return False

from collections import deque

# BFS
def bfs(graph, start, visited):
	# 큐 구현을 위해 deque 라이브러리 사용
	queue = deque([start])
	# 현재 노드를 방문 처리
	visited[start] = True

	# 큐가 빌때까지 반복
	while queue:
		v = queue.popleft()
		print(v, end=' ')
		# 해당 원소와 인접한, 아직 방문하지 않은 원소들을 큐에 삽입
		for i in graph[v]:
			if not visited[i]:
				queue.append(i)
				visited[i] = True

li = prime_list(10001)[168:]

graph = [[] for _ in range(len(li))]

for i in range(len(li)):
    for j in range(len(li)):
        if change_poss(li[i], li[j]):
            graph[i].append(j)
