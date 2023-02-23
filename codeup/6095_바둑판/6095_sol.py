import sys
sys.stdin = open('input.txt')


# 데이터 받기
N = int(input())
matrix = [[0]*20 for _ in range(20)]

for tc in range(1, N+1):
    x,y = map(int, input().split()) # 바둑 위치
    # print(x,y)
    matrix[x][y] = 1

# x,y 바둑판 만들기
for i in range(1, 20):
    for j in range(1, 20):
        print(matrix[i][j], end=' ')
    print()

# 데이터 이용해서 바둑판에 바둑 놓기
