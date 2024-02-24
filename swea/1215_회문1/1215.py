for tc in range(1, 11):
    N = int(input())
    data = list(input() for _ in range(8))


    result = 0

    # 가로 방향 회문
    for i in range(8):
        for j in range(8-N+1):
            list_1 = [0] * N
            list_2 = []
            for k in range(N):
                list_1[k] = data[i][j+k]
                list_2.append(list_1[k])
            list_2.reverse()
            if list_1 == list_2:
                result += 1

    # 세로 방향 회문
    for i in range(8):
        for j in range(8-N+1):
            list_1 = [0] * N
            list_2 = []
            for k in range(N):
                list_1[k] = data[j+k][i]
                list_2.append(list_1[k])
            list_2.reverse()
            if list_1 == list_2:
                result += 1
    print(f'#{tc}', result)