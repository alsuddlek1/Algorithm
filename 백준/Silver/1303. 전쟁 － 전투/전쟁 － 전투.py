m, n = map(int, input().split())
data = [list(input()) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def dfs(x, y, color):
    stack = [(x, y)]
    visited[x][y] = 0
    count = 1

    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    while stack:
        cx, cy = stack.pop()
        for dx, dy in zip(dxs, dys):
            nx = cx + dx
            ny = cy + dy
            if in_range(nx, ny) and visited[nx][ny] == -1 and data[nx][ny] == color:
                visited[nx][ny] = 0
                stack.append((nx, ny))
                count += 1
    return count

w, b = 0, 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == -1:
            color = data[i][j]
            size = dfs(i, j, color)
            if color == 'W':
                w += size * size
            else:
                b += size * size

print(w, b)
