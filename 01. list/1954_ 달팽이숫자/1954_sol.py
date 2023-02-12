import sys
sys.stdin = open('input.txt')

T = int(input())

    # 우, 하, 좌, 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for tc in range(1, T+1):
    N = int(input())
    matrix = [[0]*N for _ in range(N)] # 달팽이 껍질

    count = 1
    x, y = 0, 0
    dir = 0
    matrix[x][y] = count
    while count < N**2:
        nx = x + dx[dir]
        ny = y + dy[dir]
        if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] == 0:
            count += 1
            matrix[nx][ny] = count
            x, y = nx, ny
        else:
            dir += 1
            if dir >= 4:
                dir = 0
    for i in matrix:
        print(i)