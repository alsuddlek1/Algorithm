import sys
sys.stdin = open('sample_input.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def aa(i, res, x, y):
    if i == 6:
        sset.add(res)
        return

    else:
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < 4 and 0 <= ny < 4:
                aa(i+1, res*10+data[nx][ny], nx, ny)

T = int(input())
for tc in range(1, T+1):
    data = [list(map(int, input().split())) for _ in range(4)]

    sset = set()
    for i in range(4):
        for j in range(4):
            aa(0, data[i][j], i, j)
    print(len(sset))