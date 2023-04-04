import sys
sys.stdin = open('input.txt')

def aa(i, R):
    global ans
    if i == N:
        ans = max(R, ans)
        return

    if R <= ans:
        return

    else:
        for j in range(N):
            if visited[j] == 0:
                visited[j] = 1
                aa(i+1, R * arr[i][j] * 0.01)
                visited[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    visited = [0] * N
    aa(0, 1)
    print(f'#{tc} {format(100*ans, ".6f")}')