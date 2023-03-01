import sys
sys.stdin = open('input.txt')

T = int(input()) # 테스트 케이스

dx = [0, 1, 0, -1] # 우,하,좌,상
dy = [1, 0, -1, 0] # 달팽이 껍질은 우, 하 ,좌 ,상 순서로 움직임
for tc in range(1, T+1):
    # N : 달팽이의 N*N 배열
    N = int(input())
    snail = [[0]*N for _ in range(N)]
    x, y = 0, 0  # 달팽이는 무조건 0, 0에서 시작
    # x : 현재 달팽이 행 인덱스
    # y : 현재 달팽이 열 인덱스
    dir = 0  # dx, dy의 인덱스 (방향 결정해줄거임)
    cnt = 1 # 달팽이 껍직에 넣어줄 값
    snail[x][y] = cnt
    # 달팽이 시작점

# 달팽이 껍질 만들기
    while cnt < N**2:
    # 달팽이 껍질값이 N제곱보다 작을때까지 반복
    # 9번까지 채우긴 하지만, 이동 횟수는 8번임
        nx = x + dx[dir]
        # nx : 이전 행인덱스에서 dx(방향)으로 이동하는 행 인덱스
        ny = y + dy[dir]
        # ny : 이전 열인덱스에서 dy(방향)으로 이동하는 열 인덱스
        if 0 <= nx < N and 0 <= ny < N and snail[nx][ny] == 0:
            # 0 <= nx < N and 0 <= ny < N
            # 기본 델타 조건 (근데 이유 모르겠음) (아마 기본 matrix 안에 있는 범위인듯)
            # snail[nx][ny] == 0
            # 0 이 아니라면 이미 방문한 적이 있는 곳이므로(이미 숫자 할당됨) 0 일때만 이동
            cnt += 1 # 이전 수 += 1
            snail[nx][ny] = cnt  # 달팽이에 할당
            x, y = nx, ny
            # nx, ny를 현재 위치로 재 할당해주고 다시 이동함
        else:
            dir += 1
            # 이미 방문 한 적이 있는 곳, 또는 벽을 만났다면 방향 바꿔줌
            if dir >= 4:
                dir = 0 # 만약 dir이 4가 넘는다면 다시 0으로 돌아가서 회전함

    print(f'#{tc}')
    for i in snail:
        print(*i)

