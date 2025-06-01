from collections import deque

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs(x, y):
    dxs = [-1, -1, -1, 0, 0, 1, 1, 1]  # 좌상, 상, 우상, 좌, 우, 좌하, 하, 우하
    dys = [-1, 0, 1, -1, 1, -1, 0, 1]
    dist = [[-1]*m for _ in range(n)]
    q = deque()

    for i in range(n):
        for j in range(m):
            if data[i][j] == 1:
                q.append((i, j))
                dist[i][j]= 0

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if in_range(nx, ny) and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

    return dist

dist = bfs(n, m)
answer = 0
for i in dist:
    answer = max(answer, max(i))

print(answer)