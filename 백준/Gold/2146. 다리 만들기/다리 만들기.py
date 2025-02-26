# 0. 변수설정
N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상,하,좌,우
dxs = [-1, 1, 0, 0] # 상,하,좌,우
dys = [0, 0, -1, 1]

island_id = 2
result = float('inf')

# 범위
def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

# 1. 섬 구분
def dfs(x, y, island_id):
    stack = [(x, y)]
    visited[x][y] = True
    data[x][y] = island_id
    while stack:
        cx, cy = stack.pop()
        for dx, dy in zip(dxs, dys):
            nx = cx + dx
            ny = cy + dy
            if in_range(nx, ny) and not visited[nx][ny] and data[nx][ny] == 1:
                visited[nx][ny] = True
                data[nx][ny] = island_id
                stack.append((nx, ny))

# 2. 최단거리
def bfs(island_id):
    queue = []
    distance = [[-1] * N for _ in range(N)]

    # 현재 섬의 가장자리 큐에 추가
    for i in range(N):
        for j in range(N):
            if data[i][j] == island_id:
                queue.append((i, j))
                distance[i][j] = 0

    # BFS 시작
    while queue:
        x, y = queue.pop(0)  # 앞에서 꺼내기 (FIFO)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                # 바다를 만난 경우
                if data[nx][ny] == 0 and distance[nx][ny] == -1:
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))
                # 다른 섬에 도착한 경우
                if data[nx][ny] > 0 and data[nx][ny] != island_id:
                    return distance[x][y]
    return float('inf')

# 1-2. 섬구분
for i in range(N):
    for j in range(N):
        if data[i][j] == 1 and not visited[i][j]:
            dfs(i, j, island_id)
            island_id += 1

# 2-2. 최단거리 - BFS 호출
for i in range(2, island_id):
    if bfs(i) < result:
        result = bfs(i)

print(result)