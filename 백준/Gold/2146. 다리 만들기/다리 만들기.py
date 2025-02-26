# 방향 벡터 (상, 하, 좌, 우)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# DFS로 섬 구분하기
def dfs(x, y, island_id):
    stack = [(x, y)]
    visited[x][y] = True
    graph[x][y] = island_id  # 섬 번호 부여
    while stack:
        cx, cy = stack.pop()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = True
                graph[nx][ny] = island_id
                stack.append((nx, ny))

# BFS로 최단 다리 찾기
def bfs(island_id):
    queue = []
    distance = [[-1] * N for _ in range(N)]
    
    # 현재 섬의 가장자리 큐에 추가
    for i in range(N):
        for j in range(N):
            if graph[i][j] == island_id:
                queue.append((i, j))
                distance[i][j] = 0

    # BFS 시작
    while queue:
        x, y = queue.pop(0)  # 앞에서 꺼내기 (FIFO)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                # 바다를 만난 경우
                if graph[nx][ny] == 0 and distance[nx][ny] == -1:
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))
                # 다른 섬에 도착한 경우
                if graph[nx][ny] > 0 and graph[nx][ny] != island_id:
                    return distance[x][y]
    return float('inf')

# 입력 받기
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

# 1. DFS로 섬 구분하기
island_id = 2  # 섬 번호는 2부터 시작 (1은 초기 육지 번호)
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            dfs(i, j, island_id)
            island_id += 1

# 2. BFS로 각 섬에서 최단 거리 찾기
result = float('inf')
for i in range(2, island_id):
    result = min(result, bfs(i))

# 3. 최단 거리 출력
print(result)
