import sys
sys.stdin = open('input.txt')

A, B = map(int, input().split())    # 종이의 가로, 세로 길이
N = int(input()) # 잘라야 하는 점선의 개수
data = [[0]*(A+1) for _ in range(B+1)]

row = [0, B]    # 가로
col = [0, A]    # 세로
for _ in range(N):
    C, D = map(int, input().split()) # C : 가로,세로 D : 점선 번호
    if C == 0:
        row.append(D)
    else:
        col.append(D)


row.sort() # 잘라야할 가로 점선
col.sort() # 잘라야할 세로 점선
# print(row) # [0, 2, 3, 8]
# print(col) # [0, 4, 10]

ROW = 0 # 가로 최대길이
for i in range(1, len(row)):
    if row[i] - row[i-1] > ROW:
        ROW = row[i] - row[i-1]
# print(ROW) # 5

COL = 0 # 세로 최대길이
for j in range(1, len(col)):
    if col[j] - col[j-1] > COL:
        COL = col[j] - col[j-1]
# print(COL)

result = ROW * COL
print(result)

