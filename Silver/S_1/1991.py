N = int(input())

nodes = [[] for _ in range(N)]

for _ in range(N):
    parent, left, right = input().split()
    nodes[ord(parent) - ord('A')].append(ord(left) - ord('A'))
    nodes[ord(parent) - ord('A')].append(ord(right) - ord('A'))

def preorder(N):
    if N == -19:
        return
    print(chr(ord('A')+N),end='')
    preorder(nodes[N][0])
    preorder(nodes[N][1])
    
def inorder(N):
    if N == -19:
        return
    inorder(nodes[N][0])
    print(chr(ord('A')+N),end='')
    inorder(nodes[N][1])

def postorder(N):
    if N == -19:
        return
    postorder(nodes[N][0])
    postorder(nodes[N][1])
    print(chr(ord('A')+N),end='')

preorder(0)
print()
inorder(0)
print()
postorder(0)