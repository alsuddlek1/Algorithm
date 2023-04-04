import sys
sys.stdin = open('sample_input.txt')

def aa(i, res):
    global result
    if i == N:
        result = min(res, result)
        return

    if res > result:
        return

    else:
        for j in range(N):
            if visited[j] == 0:
                visited[j] = 1
                aa(i+1, res+data[i][j])
                visited[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    result = 1000000000
    aa(0, 0)
    print(result)