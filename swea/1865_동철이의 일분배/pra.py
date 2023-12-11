import sys
sys.stdin = open('input.txt')

def aa(i, P):
    global max_p
    if i == N:
        max_p = max(max_p, P)
        return

    if max_p >= P:
        return

    else:
        for j in range(N):
            if visited[j] == 0:
                visited[j] = 1
                aa(i+1, P*data[i][j]*0.01)
                visited[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    visited = [0]*N
    max_p = 0
    aa(0, 1)
    print(f'#{tc} {max_p}')