import sys
sys.stdin = open('sample_input.txt')

dx = [-1, 1, 0, 0] # 상,하,좌,우 방향 조사
dy = [0, 0, -1, 1]

def maze(x,y):
    stack = [(x,y)]
    visited = [[0]*N for _ in range(N)]
    # 미로와 같은 크기의 2차원 배열으로 내가 이동한 길을 보여줌
    while stack:
        x,y = stack.pop() # stack에서 x,y 꺼내기
        if visited[x][y] == 0: # x,y 가 내가 방문한 적이 없는(0) 인덱스라면 값을 1로 바꿔줌
            visited[x][y] = 1
        for i in range(4): # 4방향 조사
            nx = x + dx[i]
            ny = y + dy[i] # nx, ny : 이동할 인덱스
            if 0 <= nx < N and 0 <= ny < N and data[nx][ny] != 1 and visited[nx][ny] != 1:
                # 미로에서도 1이면 이동 불가능, visited에서도 1이면 이동 불가능
                if data[nx][ny] == 3: # 3이면 도착이므로 1 반환
                    return 1
                visited[nx][ny] = 1 # 3이 아니라면 visited 위치에 1을 넣어서 경로 표기
                stack.append((nx,ny)) # stack에 nx, ny를 넣어주고 다시 돌아감 이때 nx, ny는 다시 x,y가 됨
    return 0 # 끝까지 돌때까지 1이 반환 안되면 0 반환

T = int(input()) # 테스트 케이스
for tc in range(1, T+1):
    N = int(input()) # 미로의 크기(data의 크기)
    data = [list(map(int, input())) for _ in range(N)]
    # N*N 크기의 미로

    for i in range(N):
        # i : data의 행 인덱스
        for j in range(N):
            # j : data의 열 인덱스
            if data[i][j] == 2:
                # data[i][j] ==2 : i,j 값이 2일때 시작점이므로 함수 maze 실행
                print(f'#{tc}', maze(i,j))
