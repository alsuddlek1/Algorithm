data = [list(map(int, input().split())) for _ in range(10)]

# 시작점 (1,1)
y = 1
x = 1

while True:
    ## 이동이 멈추는 경우
    # 먹이 도착
    if data[y][x] == 2:
        data[y][x] = 9
        break

    # 길이 없음
    elif data[y+1][x] == 1 and data[y][x+1] == 1:
        data[y][x] = 9
        break

    # 두 경우 제외하고 이동할 때 변경
    data[y][x] = 9

    ## 길 없을 때 방향 바꾸기
    # y축 길이 없으면 x축 +=1
    if data[y+1][x] == 1:
        x += 1
    elif data[y][x+1] == 1:
        y += 1
    else:
        x += 1

for i in range(10):
    for j in range(10):
        print(data[i][j], end= " ")
    print()