# ladder1

import sys
sys.stdin = open('input.txt')

# 하,좌,우
dx = [1, 0, 0]
dy = [0, -1, 1]

def sesarch(x,y):
    visited = [[0]*100 for

    while x != 99:
        for i in range(5):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 100 and 0 <= ny < 100 and data[nx][ny] ==1 :
                x, y = nx, ny
    if data[x][y] == 2:
        return original_y
    else:
        return 0
