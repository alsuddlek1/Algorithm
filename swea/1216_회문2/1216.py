for tc in range(1, 11):
    TC = int(input())
    data = list(input() for _ in range(8))

    result = []
    N = 8

    # 가로 회문
    print("N",N)
    for i in range(8):
        # if result != 0:
        #     break
        for j in range(8-N+1):
            list_1 = [0]*N
            list_2 = []
            for k in range(N):
                print("k", k)
                list_1[k] = data[i][j+k]
                list_2.append(list_1[k])
                print("list_1",list_1)
            list_2.reverse()
            if list_1 == list_2:
                result.append(len(list_1))
                print("qwer",list_1)
                N -= 1
            else:
                N -= 1

    # 세로 회문
    for i in range(8):
        # if result != 0:
        #     break
        for j in range(8-N+1):
            list_1 = [0]*N
            list_2 = []
            for k in range(N):
                list_1[k] = data[j+k][i]
                list_2.append(list_1[k])
            list_2.reverse()
            if list_1 == list_2:
                result.append(len(list_1))
                break
            else:
                N -= 1
    print(result)
    print(tc, max(result))