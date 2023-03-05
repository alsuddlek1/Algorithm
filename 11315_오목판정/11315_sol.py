import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = [list(input()) for _ in range(N)]
    # print(data)

    result = 0 # 마지막 확인

    # 가로
    for i in range(N):
        cnt = 0
        for j in range(N):
            if data[i][j] == 'o':
                cnt += 1
        if cnt >= 5:
            result += 1

    # 세로
    for i in range(N):
        cnt = 0
        for j in range(N):
            if data[j][i] == 'o':
                cnt += 1
        # print(cnt)
        if cnt >= 5:
            result += 1

    # 좌 -> 우 대각선
    cnt = 0
    for i in range(N):
        if data[i][i] == 'o':
            cnt += 1
    # print(cnt)
        if cnt >= 5:
            result += 1

    # 우 -> 좌 대각선
    cnt = 0
    for i in range(N):
        if data[i][N-i-1] == 'o':
            cnt += 1
        # print(cnt)
        if cnt >= 5:
            result += 1

    # 최종 결과 값
    if result >= 1:
        print(f'#{tc}', 'YES')
    else:
        print(f'#{tc}', 'NO')