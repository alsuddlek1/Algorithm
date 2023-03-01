import sys
sys.stdin = open('input.txt')

T = int(input())
# 색종이 수
matrix = [[0]*100 for _ in range(100)]
# 도화지

for tc in range(1, T+1):
    x, y = map(int,input().split())
    # 색종이 붙어있는 위치
    # x : 색종이 시작하는 matrix의 인덱스
    for i in range(x,x+10):
        for j in range(y, y+10):
            matrix[i][j] += 1


count = 0
for i in range(100):
    for j in range(100):
        if matrix[i][j] >= 1:
            count += 1

print(count)