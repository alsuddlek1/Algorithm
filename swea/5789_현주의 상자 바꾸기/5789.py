import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, Q = map(int,input().split())
    # N : 상자의 개수
    # Q : L,R을 반복할 횟수
    matrix = [0] * (N + 1)  # i가 들어갈 N 길이의 배열

    for i in range(1, Q+1):
        # i : matrix에 L부터 R에 넣을 값
        L, R = map(int, input().split())
        # L,R : i 값을 넣어줄 양 끝값으로 N의 인덱스(1부터)
        for j in range(L, R+1):
            # j : i값을 넣을 matrix 인덱스
            matrix[j] = i

    result = [] # 인덱스 1부터 N까지인 최종 결과
    for k in range(1, N+1):
        result.append(matrix[k])

    print(f'#{tc}', *result)

