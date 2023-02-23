import sys
sys.stdin = open('input.txt')

# 데이터받기
h,w = map(int,input().split()) # 격자판 세로, 가로
n = int(input()) # 막대 개수
# 격자판 만들기
matrix = [[0] * w for _ in range(h)]
for nn in range(n):
    l, d, x, y = map(int, input().split())
    # print(l,d,x,y)

# 막대 방향, 크기
    for i in range(l):
        if d == 0:
            matrix[x-1][y-1+i] = 1
        elif d == 1:
            matrix[x-1+i][y-1] = 1

# 격자판에 넣기
for i in range(h):
    for j in range(w):
        print(matrix[i][j], end=' ')
    print()
