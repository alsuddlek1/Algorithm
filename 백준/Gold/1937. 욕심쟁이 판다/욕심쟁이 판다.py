# 0. 변수설정
n = int(input())
data = list(list(map(int, input().split())) for _ in range(n))
result = 0
dp = [[0] * n for _ in range(n)]

# 1-1. 범위
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 1. dfs
dxs = [-1, 1, 0, 0] # 상,하,좌,우
dys = [0, 0, -1, 1]

def dfs(x, y):
    if dp[x][y]:
        return dp[x][y]
    dp[x][y] = 1
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if in_range(nx, ny) and data[x][y] < data[nx][ny]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
    return dp[x][y]

# 2. dfs 호출
for i in range(n):
    for j in range(n):
        result = max(result, dfs(i, j))

print(result)