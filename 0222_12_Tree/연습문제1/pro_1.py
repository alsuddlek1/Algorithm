import sys
sys.stdin = open('input.txt')

def preorder(node): # 전위순회
    if node != 0:
        # 전위 순회기 때문에 내가 할일 먼저 한다.
        # 지금 문제에서 할일은? 나를 출력
        print(node, end=' ')
        # 왼쪽 자식을 조사
        preorder(left[node])
        # 오른쪽 자식을 조사
        preorder(right[node])

def inorder(node): # 중위순회
    if node != 0:
        # 왼쪽 자식을 조사
        inorder(left[node])
        # 중위 순회
        print(node, end=' ')
        # 오른쪽 자식을 조사
        inorder(right[node])

def postorder(node): # 후위순회
    if node != 0:
        # 왼쪽 자식을 조사
        postorder(left[node])
        # 오른쪽 자식을 조사
        postorder(right[node])
        # 후위 순회
        print(node, end=' ')

V = int(input())        # 노드의 개수
E = V - 1               # 간선의 개수
edge = list(map(int, input().split()))
print(edge)

# 인접행렬 => 2차원 행렬 사용했ㅈㅣ만 지금은 X

# 인덱스를활용할 것이기 때문에 V + 1 (0번 노드는 없음)
parent = [0] * (V+1)    # 부모의 정보
left = [0] * (V+1)      # 왼쪽 자식 정보
right = [0] * (V+1)     # 오른쪽 자식 정보

# 리스트 세개 만들기 귀찮으면 이렇게도~
# Tree = [[0]*3 for _ in range(V+1)]
# print(Tree)

for i in range(E):
    p, c = edge[i*2], edge[i*2+1]
    if left[p] == 0:    # 아직 왼쪽 자식이 없으면
        left[p] = c     # p번의 왼쪽 자식 c
    else:
        right[p] = c
    parent[c] = p

    # if Tree[p][0] == 0:
    #     Tree[p][0] = c
    # else:
    #     Tree[p][1] = 3
    # Tree[c][2] == p
# print(Tree)

# 루트찾기
root = 0
for i in range(1, V+1): # 모든 노선 순회
    # 부모정보를 담았는데 부모가 없으면 루트
    if parent[i] == 0:
        root += 1
        break

print(left)
# 조사를 시작 root 노드부터
preorder(root)
print()
inorder(root)
print()
postorder(root)