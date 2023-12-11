import sys
sys.stdin = open('sample_input.txt')

dx = [0, 1, 1, 1] # 좌우상하 다 볼필요 X
dy = [1, 1, 0, -1] # 우, 하, 우하, 좌하 일케만 보면댐

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = [list(input()) for _ in range(N)]

    result = 0 # 최종 오목 결과 판단
    for x in range(N):
        # x : data의 행 인덱스
        for y in range(N):
            # y : data의 열 인덱스
            if data[x][y] == 'o':
                # 오목이 배치되어있을때
                for i in range(4):
                    cnt = 0
                    for j in range(1,5): # 5개 이상일때 오목(17줄에서 이미 하나 있음)
                        nx = x + dx[i]*j
                        ny = y + dy[i]*j
                        if 0 <= nx < N and 0 <= ny < N and data[nx][ny] == 'o':
                            cnt += 1
                    if cnt >= 4: # cnt가 4 이상이면 오목
                        result += 1
    if result >= 1: # 한 배열에 오목이 1개 이상일때
        print(f'#{tc}', 'YES')
    else:
        print(f'#{tc}', 'NO')