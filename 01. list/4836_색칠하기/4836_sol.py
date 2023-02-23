import sys
sys.stdin = open('input.txt')

# 3이 될때 보라색 색칠해서 보라색 몇개?

# 1. input
T = int(input())
# 2. matrix 위에 색칠하기
for tc in range(1, T+1):
    N = int(input())
    matrix = [[0] * 10 for _ in range(10)]
    result = 0  # 보라색 개수

    for tcc in range(N):
        r1, c1, r2, c2, col = map(int,input().split())
        # print(x1, x2, y1, y2, c)
        for x in range(r1, r2+1):
            for y in range(c1, c2+1):
                matrix[x][y] += col
                if matrix[x][y] == 3:
                    result += 1
    print(result)


