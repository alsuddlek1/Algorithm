import sys
sys.stdin = open('in1.txt')

T = int(input())

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

for tc in range(1, T+1):
    N, M = map(int,input().split())
    data = [list(map(int, input().split())) for _ in range(N)]

    maxV = 0  # 최종 최대값
    for x in range(N):  # x : data의 행 인덱스
        for y in range(N):  # y : data의 열 인덱스
            cnt = data[x][y]
            for i in range(4):
                for j in range(1,M): # 상,하,좌,우 +자 모양 조사
                    nx = x + dx[i]*j
                    ny = y + dy[i]*j
                    if 0 <= nx < N and 0 <= ny < N:
                        cnt += data[nx][ny]
            if maxV < cnt:
                maxV = cnt

    for x in range(N):  # x : data의 행 인덱스
        for y in range(N):  # y : data의 열 인덱스
            cnt = data[x][y]
            for i in range(4,8):
                for j in range(1,M): # X자 모양 조사
                    nx = x + dx[i]*j
                    ny = y + dy[i]*j
                    if 0 <= nx < N and 0 <= ny < N:
                        cnt += data[nx][ny]
            if maxV < cnt:
                maxV = cnt

    print(f'#{tc} {maxV}')