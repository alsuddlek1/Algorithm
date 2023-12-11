import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 농장의 크기
    data = [list(map(int,input())) for _ in range(N)]
    # N*N인 농장 행렬

    result = 0 # 농장 전체의 수익
    for i in range(N):
        # i : data의 행 인덱스
        for j in range(abs(N//2-i), N-abs(N//2-i)):
            # j : data의 열 인덱스
            # print(j) # 2, 123, 01234 ,,,
            result += data[i][j]

    print(f'#{tc} {result}')