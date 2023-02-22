import sys
sys.stdin = open('sample_input.txt')

## 노드N을 루트로 하는 서브 트리에 속한 노드의 개수

# 3. 전위 순회
def preorder(node):
    if node != 0:
        # 전위 순회기 때문에 내가 할일 먼저 한다.
        # 지금 문제에서 할일은? 나를 출력
        print(node, end=' ')
        # 왼쪽 자식을 조사
        preorder(left[node])
        # 오른쪽 자식을 조사
        preorder(right[node])

# 1. 데이터 받아오기
T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split()) # E:간선, N:서브트리의 루트노드
    V = E + 1  # 전체 노드의 개수
    edge = list(map(int, input().split()))

# 2. 배열을 이용해서 이진 트리 표현 (부모 번호를인덱스로 자식번호 저장)
    parent = [0] * (V+1)
    left = [0] * (V+1)
    right = [0] * (V+1)

    for i in range(E):
        p, c = edge[i*2], edge[i*2+1]
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c
        parent[c] = p

    root = 0
    for i in range(1, V+1):
        if parent[i] == 0:
            root = 1
            break

    preorder(root)