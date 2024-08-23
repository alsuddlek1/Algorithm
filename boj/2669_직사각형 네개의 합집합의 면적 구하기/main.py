import sys
sys.stdin = open('input.txt')

matrix = [[0]*100 for _ in range(100)]  # 100*100 배열
result = 0

for _ in range(4):
    x1, y1 , x2, y2 = map(int,input().split())
# x1, y1 : 사각형 왼쪽 아래 꼭짓점
# x2, y2 : 사각형 오른쪽 위 꼭짓점
    for i in range(x1, x2):
        for j in range(y1,y2):
            matrix[i][j] += 1
            # print(matrix)
            # if matrix[i][j] >= 1:
            result +=1

print(result)