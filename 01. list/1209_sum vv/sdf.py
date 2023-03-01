import sys
sys.stdin = open('input.txt')

# 가로, 세로, 좌우 대각선 총 4개 합 중 최댓값 출력

# input
for tc in range(10):
    tc = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]

    result = 0
# 가로
    for x in range(100):
        a = 0
        for y in range(100):
            a += arr[x][y]
            if a > result:
                result = a
# 세로
    for x in range(100):
        a = 0
        for y in range(100):
            a += arr[y][x]
            if a > result:
                result = a
# 좌-> 우 대각선
    for x in range(100):
        a = 0
        a += arr[x][x]
        if a > result:
            result = a
# 우->좌 대각선
    for x in range(100):
        a = 0
        a += arr[x][99-x]
        if a > result:
            result = a

    print(f'#{tc} {result}')