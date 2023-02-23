import sys
sys.stdin = open('input.txt')

# 수학적좌표 기준 (2.2) 에서 출발해서 2 도착하면 출력

# 2. 미로 문제니까 델타 이용 오른쪽 아래로만 이동
dx = [0, 1]
dy = [1, 0]

# 3. maze 함수 이용 스택 팝 => DFS?
def maze(x,y):
    stack = [(x, y)]
    visited[x][y] = 1
    while stack:
        x, y = stack.pop()
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if data[nx][ny] != 1:
                data[nx][ny] = 9
                if data[nx][ny] == 2:
                    break
                data[nx][ny] = 1
                # pprint(maze)
                stack.append((nx, ny))
    # return 0
# 1. 데이터 받기
    # 시작점 (2,2), 10*10 미로, 이동경로 = 9
data = [list(map(int,input().split())) for _ in range(10)]
# print(data)
visited = [[0]*10 for _ in range(10)]

# 4. 2일때 도착 출력
for i in range(10):
    for j in range(10):
        if data[i][j] == 2:
            print(maze(i, j))