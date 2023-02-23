import sys
sys.stdin = open('input.txt')

# 뒤집기한 결과 출력
# 데이터 받기 (1. 바둑판 19줄, 2. 십자뒤집기 횟수 3. 뒤집을(?) 좌표
# 좌표를 제외하고 다 바꿔주나?

matrix = [list(map(int, input().split())) for _ in range(19)]

T = int(input())
for tc in range(1, T+1):
    x, y = map(int, input().split())
    for i in range(19):
        for j in range(19):
            if matrix[i][x-1] == 1:
                matrix[i][x-1] = 0
            else:
                matrix[i][x-1] = 1
            if matrix[y-1][j] == 1:
                matrix[y-1][j] = 0
            else:
                matrix[y-1][j] = 1
    # x, y의 인풋값은 일반적인 수학에서 쓰는 행렬 좌표라서
    # 행렬의 좌표에서 +1 씩 한게 x, y값임
    # 그니까 y - 1 = i, x - 1 = j 임
    # 그래서 그거 바꿔 주면 됨
for i in range(19):
    for j in range(19):
        print(matrix[i][j], end=' ')
    print()
    #     print(*matrix[i])






