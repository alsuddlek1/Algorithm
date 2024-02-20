for tc in range(10):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]
    result = 0

    #가로, 세로
    for i in range(100):
        width = 0
        height = 0
        left_cross = 0
        right_cross = 0
        for j in range(100):
            # 가로
            width += data[i][j]
            if width >= result:
                result = width
            # 세로
            height += data[j][i]
            if height >= result:
                result = height
            # 왼쪽 -> 오른쪽
        left_cross += data[i][i]
        if left_cross >= result:
            result = left_cross
        # 오른쪽 -> 왼쪽
        right_cross += data[99-i][99-i]
        if right_cross >= result:
            result = right_cross

    print(f'#{tc+1} {result}')