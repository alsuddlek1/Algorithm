import sys
sys.stdin = open('input.txt')

## 이웃한 값의 차의 절대값의 합의 총합구하기

# 2. 델타 조사(상,하,좌,우) => 차의 절대값 구하기
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

# 검색함수
def serch(x,y,N):
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            cnt += abs(arr[nx][ny] - arr[x][y])
    return cnt


# 1. 데이터 받기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(N):
            result += serch(i,j,N)
    print(result)