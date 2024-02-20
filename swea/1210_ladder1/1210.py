for tc in range(10):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]

    dx = [1, 0, 0]
    dy = [0, 1, -1]
    result = 0

    for i in range(100):
        if data[0][i] == 1:
            x, y = 0, i
            cnt = 0
            while x < 99:
                if cnt == 0:
                    if y > 0 and data[x][y-1]:
                        cnt = 2
                    elif y < 99 and data[x][y+1]:
                        cnt = 1
                else:
                    if data[x+1][y]:
                        cnt = 0
                x += dx[cnt]
                y += dy[cnt]
            if data[x][y] == 2:
                result = i
                break
    print(f'#{tc+1} {result}')
