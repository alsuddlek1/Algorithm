w,h = map(int, input().split()) #격자판 크기
n = int(input()) # 막대 개수
matrix = [[0]*(h+1) for _ in range(w+1)] #격자판

for _ in range(n):
    l, d, x, y = map(int, input().split()) # 막대의 길이, 막대 방향(0 : 가로), x,y 좌표
    if d == 0:
        for i in range(y, y+l):
            print(x, i)
            matrix[x][i] = 1
    else:
        for j in range(x, x+l):
            print(j,y)
            matrix[j][y] = 1

for i in range(1, w+1):
    for j in range(1, h+1):
        print(matrix[i][j], end= " ")
    print()
