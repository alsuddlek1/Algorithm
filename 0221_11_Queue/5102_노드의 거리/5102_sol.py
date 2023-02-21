import sys
sys.stdin = open('sample_input.txt')
from collections import deque

# 주어진 출발노드에서 도착 노드까지 최소 몇개의 간선?

# 2. BFS로 시작점에서부터 끝점까지 탐색

# 1) 길이 있는지 2) 방문한적 없는지
def BFS(data, S, V):
    visited = [0] * (V+1) # 방문 경험 담을거임
    queue = deque([])  # 선입선출 하려고?
    queue.append(S)
    visited[S] = 1 # 처음 방문은 1
    while queue:
        t = queue.popleft() # 큐에서 앞에 있는거 pop해서 t : data의 행
        if t == G:  # 현재 조사 대상이 도착이면 멈춤
            return visited[t] - 1

        for i in range(len(data[t])): # t행을 for 순회해 i열
            if data[t][i] and visited[i] == 0 : # 길이 있고 방문한적 없으면
                queue.append(i) # 큐에 입력(이 입력된 곳 다 조사)
                visited[i] = visited[t] + 1
    # 더 이상 조사를 하지 않는 때는 언제?
    # 길을 더 찾아야하는데 큐가 없어서 while 돌 수 없음음
    return 0

# 1. 데이터 받기
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())    # V : 노드 개수, E : 간선
    data = [[0] * (V + 1) for _ in range(V + 1)] # 좌표
    for _ in range(E):
        x, y = map(int,input().split())  # 1 4 => 1과 4 사이 이동 가능
        # 방향성이 없으므로 양방향으로, x,y 좌표에 맞춰서 길이 있을 경우 data에 1
        data[x][y] = 1
        data[y][x] = 1
    S, G = map(int,input().split())     # S : 시작점, G : 마지막점

# 4. 결과
    print(f'#{tc}', BFS(data, S, V))
