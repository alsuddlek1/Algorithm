T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    print(f'#{tc}')

    for i in range(N):
        result_90 = []
        result_180 = []
        result_270 = []
        for j in range(N):
            result_90.append(str(data[N-j-1][i]))
            result_180.append(str(data[N-i-1][N-j-1]))
            result_270.append(str(data[j][N-i-1]))

        print(''.join(result_90), ''.join(result_180), ''.join(result_270),)