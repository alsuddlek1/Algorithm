import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    # N : arr의 크기
    # M : M*M 크기의 파리채
    arr = [list(map(int, input().split())) for _ in range(N)]
        # N*N 크기의 배열

    maxV = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            cnt = 0
            for k in range(i,i+M):
                for l in range(j, j+M):
                    cnt += arr[k][l]
            # print(cnt)
            if cnt > maxV:
                maxV = cnt
    print(f'#{tc} {maxV}')