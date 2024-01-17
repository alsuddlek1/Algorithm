dx = [0, 1, 0, -1] # 우하좌상
dy = [1, 0, -1, 0]

N, M = map(int, input().split())
snail = [[0]*M for _ in range(N)]

x, y = 0, 0
dir = 0
c = 1
snail[x][y] = c

while c < N*M:
    nx = x + dx[dir]
    ny = y + dy[dir]
    if 0 <= nx < N and 0 <= ny < M and snail[nx][ny] == 0:
        c += 1
        snail[nx][ny] = c
        x,y = nx, ny
    else:
        dir += 1
        if dir >= 4:
            dir = 0

for i in range(N):
    for j in range(M):
        print(snail[i][j], end=" ")
    print()