import sys
sys.setrecursionlimit(10**6)

# 2. 범위
def in_range(x, y):
    return 0 <= x < N and 0 <= y < M

# 1. dfs
def dfs(x, y):
    dxs = [-1, 1, 0, 0]  # 상 하 좌 우
    dys = [0, 0, -1, 1]

    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if in_range(nx, ny) and matrix[nx][ny] == 1:
            matrix[nx][ny] = -1
            dfs(nx, ny)

# 0. 변수설정
T = int(input())
for t in range(T):
    M, N, K = map(int, input().split())
    matrix = [[0] * M for _ in range(N)] # 배추밭

    visited = [[0] * M for _ in range(N)]
    for _ in range(K):
        y, x = map(int, input().split()) # 배추의 위치
        matrix[x][y] = 1

    count = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1: # 배추가 있을 때
                dfs(i, j)
                count += 1

    print(count)