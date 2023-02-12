import sys
sys.stdin = open('input.txt')

for tc in range(10):
    N = int(input())
    matrix = [list(map(int,input().split())) for i in range(100)]

    result = 0

    # 행
    for i in range(100):
        cnt = 0
        for j in range(100):
            cnt += matrix[i][j]
        if result < cnt:
            result = cnt

    # 가로
    for i in range(100):
        cnt = 0
        for j in range(100):
            cnt += matrix[j][i]
        if result < cnt:
            result = cnt

    for i in range(100):
        cnt = 0
        cnt += matrix[i][i]
        if result < cnt:
            result = cnt

    for i in range(100):
        cnt = 0
        cnt += matrix[i][99-i]
        if result < cnt:
            result = cnt

    print(result)