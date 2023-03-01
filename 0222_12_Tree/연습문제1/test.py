import sys
sys.stdin = open('input.txt')

V = int(input()) # V : 정점(노드)의 개수
E = V-1 # E : 노선의 개수
tree = [[0]*3 for _ in range(V+1)]
edge = list(map(int, input().split()))

for i in range(E):
    p, c = edge[i*2], edge[i*2+1]
    # p : 부모의 노드
    # c : 자식의 노드

    if tree[p][0] == 0:
        tree[p][0] = c
    else:
        tree[p][1] = c

    tree[c][2] = p

# for i in tree:
    # print(i)

# 루트찾기
root = 0
for i in range(V+1):
    if tree[i][2] == 0:
        root = i
# print(root)

def preorder(node):
    # 전위순회
    if node != 0:
        print(node, end=' ')
        preorder(tree[node][0])
        preorder(tree[node][1])

# preorder(root)

def inorder(node):
    if node!= 0:
        inorder(tree[node][0])
        print(node, end=' ')
        inorder(tree[node][1])

def postorder(node):
    if node != 0:
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node, end=' ')