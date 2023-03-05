import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N,M = map(int, input().split())
    data = [list(map(int,input().split())) for _ in range(N)]

    maxV = 0
    for i in range(N-M+1):
        # i : data의 행 인덱스
        for j in range(N-M+1):
            # j : data의 열 인덱스
            res = 0
            for x in range(i, i+M):
                # 파리채의 행 인덱스
                for y in range(j,j+M):
                    # 파리채의 열 인덱스
                    res += data[x][y]
            # print(res)
            if res > maxV:
                maxV = res
    print(f'#{tc} {maxV}')