import sys
sys.stdin = open('input.txt')

matrix = [[0]*100 for _ in range(100)]

for tc in range(4):
    x1, y1, x2, y2 = map(int, input().split())


    for i in range(x1,x2):
        # i : 직사각형의 행 인덱스
        for j in range(y1, y2):
            # j : 직사각형의 열 인덱스
            matrix[i][j] += 1
            # 직사각형에 해당하는 matrix에 +1

result = 0
for x in range(100):
    for y in range(100):
        if matrix[x][y] > 0:
            result += 1

print(result)