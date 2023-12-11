dx = [1, 0, -1, 0]  # 하, 우, 상, 좌
dy = [0, 1, 0, -1]

C, R = map(int, input().split())    # 가로, 세로
K = int(input())    # 대기번호
data = [[0]*C for _ in range(R)]

dir = 0
x, y = 0, 0
cnt = 1
data[x][y] = cnt

result = []
while cnt == K:
    nx = x + dx[dir]
    ny = y + dy[dir]
    if 0 <= nx < C and 0 <= ny < R and data[nx][ny] == 0:
        cnt += 1
        x, y = nx, ny
        data[x][y] = cnt
    else:
        dir += 1
        if dir >= 4:
            dir = 0
print(x, y)

