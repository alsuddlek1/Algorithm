import sys
sys.stdin = open('sample_input.txt')

# 2차원 배열에서 같은 행과 열을 못볼때

def back(n, tmp):
    global cost
    if n == N:
        cost = min(tmp, cost)
        return

    if tmp > cost:
        return

    else:
        for j in range(N):
            if visited[j] == 0:
                visited[j] = 1
                back(n+1, tmp + arr[n][j])
                visited[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0]*N
    cost = 100*N*N
    back(0, 0)

    print(f'#{tc} {cost}')