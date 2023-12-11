import sys
sys.stdin = open('in1.txt')

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    # N : 배열 크기
    # M : 노즐의 중심으로 M칸 만큼 분사
    arr = [list(map(int, input().split())) for _ in range(N)]
    # data : N*N 배열
    ans = 0
    for si in range(N):
        for sj in range(N):
            cnt = arr[si][sj]
            for di, dj in ((-1, 0), (1, 0), (0,-1), (0, 1)):
                for mul in range(1, M):
                    ni, nj = si + di*mul, sj + dj*mul
                    if 0 <= ni < N and 0 <= nj < N:
                        cnt += arr[ni][nj]
            ans = max(ans, cnt)

            cnt = arr[si][sj]
            for di, dj in ((-1, -1), (1, 1), (1, -1), (1, 1)):
                for mul in range(1, M):
                    ni, nj = si + di * mul, sj + dj * mul
                    if 0 <= ni < N and 0 <= nj < N:
                        cnt += arr[ni][nj]
            ans = max(ans, cnt)

    print(f'#{tc} {ans}')