T = int(input())

for tc in range(1, T+1):
    data = [list(map(int, input().split())) for _ in range(9)]

    result = 1

    # 가로
    for i in range(9):
        num_list = [0] * 10
        for j in range(9):
            num_list[data[i][j]] += 1
            if num_list[data[i][j]] > 1:
                result = 0

    # 세로
    for i in range(9):
        num_list = [0] * 10
        for j in range(9):
            num_list[data[j][i]] += 1
            if num_list[data[j][i]] > 1:
                result = 0

    # 3x3
    for i in range(1, 4):
        num_list = [0] * 10
        for j in range(i*3-3, i*3):
            for k in range(i*3-3, i*3):
                num_list[data[j][k]] += 1
                if num_list[data[j][k]] > 1:
                    result = 0

    print(f'#{tc}',result)