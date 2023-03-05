import sys
sys.stdin = open('in1.txt')

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(N)]

    maxV = 0
    for x in range(N):
        for y in range(N):
            cnt = data[x][y]
            for i in range(4):
                for j in range(1, M):
                    nx = x + dx[i]*j
                    ny = y + dy[i]*j
                    if 0 <= nx < N and 0 <= ny < N:
                        cnt += data[nx][ny]
            if maxV < cnt:
                maxV = cnt

    for x in range(N):
        for y in range(N):
            cnt = data[x][y]
            for i in range(4,8):
                for j in range(1, M):
                    nx = x + dx[i]*j
                    ny = y + dy[i]*j
                    if 0 <= nx < N and 0 <= ny < N:
                        cnt += data[nx][ny]
            if maxV < cnt:
                maxV = cnt
    print(maxV)