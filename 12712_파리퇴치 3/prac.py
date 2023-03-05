import sys
sys.stdin = open('in1.txt')

dx = [-1, 1, 0, 0, -1, -1, 1, 1] # 상,하,좌,우,대각선
dy = [0, 0, -1, 1, -1, 1, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N,M = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(N)]

    maxV = 0 # 최대 파리 퇴치 값

    # + 모양 퇴치
    for x in range(N):
        for y in range(N):
            result = data[x][y]  # 총 파리 퇴치 값
            for i in range(4):
                for j in range(1,M):
                    nx = x + dx[i]*j
                    ny = y + dy[i]*j
                    if 0 <= nx < N and 0 <= ny < N:
                        result += data[nx][ny]
            if result > maxV:
                maxV = result
    # print(maxV)

    # x 모양 퇴치
    for x in range(N):
        for y in range(N):
            result = data[x][y]  # 총 파리 퇴치 값
            for i in range(4,8):
                for j in range(1, M):
                    nx = x + dx[i] * j
                    ny = y + dy[i] * j
                    if 0 <= nx < N and 0 <= ny < N:
                        result += data[nx][ny]
            if result > maxV:
                maxV = result

    print(f'#{tc} {maxV}')