import sys
sys.stdin = open('input.txt')

# 학생들 배정위한 최소한의 방의 수 출력

matrix = [[0] * 2 for _ in range(7)]
# 학생들의 정보 입력할 matrix, 행:성별, 열:학년
N, K = map(int, input().split())
# N : 전체 학생 수
# K : 한방에 배정할 수 있는 최대 인원 수
for tc in range(1, N+1):
    data = list(map(int, input().split()))
    # [성별, 학년] 으로 이루어진 리스트
    # S : 학생의 성별, 0:여학생, 1:남학생
    # Y : 학생의 학년 1~6

    for i in range(1,7):
        # i : 학생들의 성별 인덱스, 0,1
        for j in range(2):
            # j : 학생들의 학년 인덱스, 1,2,3,4,5,6
            # print(i, j)
            if j == data[0] and i == data[1]:
                matrix[i][j] += 1
# print(matrix)
    # matrix에서 1 이상일때, count 해서 방 개수 구하기
count = 0
for i in range(1, 7):
    # i : 학생들의 성별 인덱스, 0,1
    for j in range(2):
    # j : 학생들의 학년 인덱스, 1,2,3,4,5,6
        if matrix[i][j] > K and matrix[i][j] % 2 == 1:
            count += matrix[i][j]//2 + 1
        elif matrix[i][j] > K and matrix[i][j] % 2 == 0:
            count += matrix[i][j] // 2
        elif 0 < matrix[i][j] <= K:
            count += 1
print(count)