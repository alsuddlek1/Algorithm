data = [list(map(int, input().split())) for _ in range(25)]

result = [[0]*25 for _ in range(25)]

# 8방향 확인
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for i in range(25):
    for j in range(25):
        # 생명이 없는 칸
        if data[i][j] == 0:
            sum = 0
            for k in range(8):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < 25 and 0 <= ny < 25:
                    sum += data[nx][ny]
            # 8방향에 3마리 생명이 존재할 경우
            if sum == 3:
                result[i][j] = 1

        # 생명이 있는 칸
        elif data[i][j] == 1:
            sum = 0
            for k in range(8):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < 25 and 0 <= ny < 25:
                    sum += data[nx][ny]
            # 다음 세대 생명
            if sum == 2 or sum == 3:
                result[i][j] = 1
            else:
                result[i][j] = 0

for i in range(25):
    for j in range(25):
        print(result[i][j], end=" ")
    print()

