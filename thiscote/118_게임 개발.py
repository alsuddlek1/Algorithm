N, M = map(int, input().split())
x, y, direction = map(int, input().split())

matrix = [[0]*M for _ in range(N)]
# 1 = 바다 + 이미 지난 곳 : 이동 X, 0 = 육지 + 아직 안 간 곳 : 이동 O

matrix[x][y] = 1 # 현재 좌표 1로 변환
data = []
for i in range(N):
    data.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0] # 북동남서
dy = [0, 1, 0, -1]

# 왼쪽으로 회전하는 함수
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0 # 네번되면 갈곳없는거

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if matrix[nx][ny] == 0 and data[nx][ny] == 0: # 회전 후 갈 수 있을때
        matrix[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0

    else: # 갈수없을 때
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if data[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)
