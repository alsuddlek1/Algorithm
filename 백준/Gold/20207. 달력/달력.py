# 0. 변수설정
N = int(input())
cal = [0]*366

# 1. 달력 만들기
for i in range(N):
    s, e = map(int, input().split())
    for j in range(s, e+1):
        cal[j] += 1

# 2. 코팅지 면적 구하기
area = 0
col, row = 0, 0
for i in range(366):
    if cal[i] != 0:
        row = max(row, cal[i])
        col += 1
    else:
        area += row * col
        row = 0
        col = 0

area += row * col
print(area)