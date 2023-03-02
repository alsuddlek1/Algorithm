import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # N : N*N 배열의 크기
    data = [list(map(int,input().split())) for _ in range(N)]
    # data : N*N 크기의 행렬
    print(f'#{tc}')
    # 90도 회전
    for i in range(N):
        # i : data의 열 인덱스
        result_90 = [] #시계방향으로 90 옮긴 값들을 담을 리스트
        result_180 = []
        result_270 = []
        for j in range(N):
            # j : data의 행 인덱스
            result_90.append(str(data[N-j-1][i])) # 시계방향으로 90 옮긴 값
            result_180.append(str(data[N-i-1][N-j-1])) # 180도 옮긴 값
            result_270.append(str(data[j][N-i-1]))

        print(''.join(result_90), ''.join(result_180), ''.join(result_270),)