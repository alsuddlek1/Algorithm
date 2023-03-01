import sys
sys.stdin = open('input.txt')

T = int(input()) # 테스트 케이스
dx = [0, 1, 0, -1] # 우, 하, 좌, 상 방향으로 이동
dy = [1, 0, -1, 0]

for tc in range(1, T+1):
    N = int(input())  # 달팽이 크기
    snail = [[0]*N for _ in range(N)] # 길이가 N인 달팽이 2차원 배열
    dir = 0 # dir : dx, dy의 인덱스로 우,하,좌,상 방향결정
    x, y = 0, 0 # 달팽이 시작점 0, 0
    # x : 달팽이 배열의 행 인덱스으로 현재 달팽이 위치
    # y : 달팽이 배열의 열 인덱스으로 현재 달팽이 위치
    cnt = 1 # 달팽이 배열에 담을 수ㅡ 1~ N 까지
    snail[x][y] = cnt

    while cnt < N**2:
        # N**2개의 칸이 있으므로 그 수보다 커지면 멈춤
        nx = x + dx[dir]
        ny = y + dy[dir]
        if 0 <= nx < N and 0 <= ny < N and snail[nx][ny] == 0:
            cnt += 1
            x,y = nx, ny
            snail[x][y] = cnt
        else:
            dir += 1
            if dir >= 4:
                dir = 0
    for i in snail:
        print(*i)