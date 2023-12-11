import sys
sys.stdin = open('iniput.txt')

N = int(input()) # 색종이 수
data = [[0]*102 for _ in range(102)] # 도화지

for _ in range(N):
    A, B = map(int, input().split())

    for x in range(A, A+10):
        for y in range(B, B+10):
            data[x][y] = 1

res = 0 # 테두리 결과값
for i in data:
    # print(i) # data 한줄씩 받기
    for k in range(1, 102):
        if i[k-1] != i[k]:
            res += 1
# print(res) # 여기까지는 세로

## 전치행렬로 바꾸기 => 가로 테두리
for i in range(102):
    for j in range(102):
        if i < j:
            data[i][j], data[j][i] = data[j][i], data[i][j]

# 재 비교
for i in data:
    # print(i) # data 한줄씩 받기
    for k in range(1, 102):
        if i[k-1] != i[k]:
            res += 1

print(res)