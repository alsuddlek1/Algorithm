# 0. 변수설정
n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
res = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

# 1. dfs
def dfs(x, y):
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    stack = [(x, y)]
    area = 0
    data[x][y] = 0 # 방문처리

    while stack:
        cx, cy = stack.pop()
        area += 1
        for dx, dy in zip(dxs, dys):
            nx = cx + dx
            ny = cy + dy
            if in_range(nx, ny) and data[nx][ny] == 1:
                data[nx][ny] = 0
                stack.append((nx, ny))

    return area

# 2. 도화지 크기 찾기
for i in range(n):
    for j in range(m):
        if data[i][j] == 1:
            cnt += 1
            res = max(res, dfs(i, j))

print(cnt)
print(res)