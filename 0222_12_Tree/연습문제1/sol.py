import sys
sys.stdin = open('input.txt')


def preorder(node):
    if node != 0:
        # 전위 순회기 떄문에
        # 내가 할일 먼저 한다.
        # 지금 문제에서 할일은? 나를 출력
        print(node, end=' ')
        # 왼쪽 자식을 조사
        preorder(tree[node][0])
        # 오른쪽 자식을 조사
        preorder(tree[node][1])

def inorder(node):
    if node != 0:
        # 왼쪽 자식을 조사
        inorder(tree[node][0])
        # 중위 순회
        print(node, end=' ')
        # 오른쪽 자식을 조사
        inorder(tree[node][1])

def postorder(node):
    if node != 0:
        # 왼쪽 자식을 조사
        postorder(tree[node][0])
        # 오른쪽 자식을 조사
        postorder(tree[node][1])
        # 후위 순회
        print(node, end=' ')

V = int(input())    # 노드의 개수
E = V - 1           # 간선의 개수
edge = list(map(int, input().split()))


# 인덱스를 활용할 것이기 때문에 노드의 개수 +1
# 0번 노드는 없음
tree = [[0]*3 for _ in range(V+1)]
# print(tree)

for i in range(E):
    p, c = edge[i*2], edge[i*2+1]
    # print(p, c)

    if tree[p][0] == 0: # 왼쪽자식이 없으면
        tree[p][0] = c # 왼쪽자식을 넣어줌
    else:
        tree[p][1] = c # 왼쪽자식이 잇으면 오른쪽 자식

    tree[c][2] = p # 이때 자식들의 부모는 p

for i in tree:
    print(i)


# 루트찾기
root = 0
for i in range(1, V+1):     # 모든 노드 순회
    # 부모정보를 담았는데, 부모가 없으면 루트
    if tree[i][2] == 0:
        root = i
        break
# print(root)

# print(left)
# 조사를 시작 root 노드부터
print('---전위 순회---')
preorder(root)
print()
print('---중위 순회---')
inorder(root)
print()
print('---후위 순회---')
postorder(root)
