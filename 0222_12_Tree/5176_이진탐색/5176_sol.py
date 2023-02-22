import sys
sys.stdin = open('sample_input.txt')


# 완전 이진 트리로 만든 후 1) 루트 값과 2) N/2번 노트 출력

# 3. 중위순회 함수
def inorder(node):
    global rlt
    if node != 0:
        inorder(left[node])
        # print(node, end=' ')
        rlt.append(node)
        inorder(right[node])

# 1. 데이터 받기
T = int(input())
for tc in range(1, T+1):
    N = int(input())    # N : 노드 개수
    E = N - 1           # E : 간선 개수
    edge = list(range(1, N+1))
    rlt = []

# 2. 완전 이진 트리 만들기
    parent = [0] * (N+1)    # 부모의 정보
    left = [0] * (N+1)      # 왼쪽 자식 정보
    right = [0] * (N+1)     # 오른쪽 자식 정보

    for i in range(1, N+1): # 규칙찾기
        # i = 0 1 2 3 4 5 6
        # p = 0 0 1 1 2 2 3
        # l = 0 2 4 6 0 0 0
        # r = 0 3 5 0 0 0 0
        parent[i] = i//2
        left[i] = i*2
        right[i] = i*2+1
        # N 넘으면 다 0으로 만들어주기
        if left[i] > N:
            left[i] = 0
        if right[i] > N:
            right[i] = 0

    root = 0
    for i in range(1, N+1): # 모든 노선 순회
        # 부모정보를 담았는데 부모가 없으면 루트
        if parent[i] == 0:
            root = 1
            break

    inorder(root)
    print(rlt)
    # print()
    # print(parent)
    # print(left)
    # print(right)


# 4. 루트값, N/2번출력
# 부모가 없을때 루트 => parent[i] = 0 일때 루트
#     for i in range(1, N+1):
#         if parent[i] == 0:
#             print(rlt[i-1])