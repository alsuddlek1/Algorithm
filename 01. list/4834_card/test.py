import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # aii = list(map(int, input().split())) # [49679]
    ai = list(map(int, input()))            # [4, 9, 6, 7, 9]

    matrix = [0]*10
    max_count = 0
    max_val = 0
    for i in ai:
        # print(i) # 4 9 6 7 9
        matrix[i] += 1 # 1 1 1 1 2 : 방문 횟수마다 1 증가
        if max_count < matrix[i]:
            max_count = matrix[i]
            max_val = i
            # print(max_val) 이게뭐지
        elif max_count == matrix[i] and max_val < i:
            max_count = matrix[i]
            max_val = i

    print(f'#{tc} {max_val} {max_count}')
