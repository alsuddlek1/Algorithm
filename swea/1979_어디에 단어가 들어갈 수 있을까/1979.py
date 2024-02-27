T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]

    result = 0

    for i in range(N):
        for j in range(N-M+1):
            M_list = [0] * M

            # 1로 시작하면 데이터 담기
            if data[i][j] == 1:
                for k in range(j, j+M):
                    # k = j, j+1, j+2 ,,
                    for l in range(M):
                        M_list[l] = data[i][k]
            print(M_list)

            # M_list에서 0이 없다면
            for k in range(M):
                if M_list[k] != 1:
                    print("break")
                    break
                else:
                    if j+M+1 < N and data[i][j+M+1] == 1:
                        print("1이 네개이상일때", data[i][j])
                        break
                    elif j+M+1 < N and data[i][j+M+1] == 0:
                        result += 1
                        print("0이 세개일때",result, data[i][j])
    print(result)