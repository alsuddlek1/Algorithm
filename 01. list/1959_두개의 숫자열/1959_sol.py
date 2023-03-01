import sys
sys.stdin = open('input.txt')

# 마주보는 수의 곱의 최대값

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # N : 숫자열 ai의 숫자개수
    # M : 숫자열 bj의 숫자개수
    ai = list(map(int, input().split()))
    # ai : N개의 숫자로 구성된 숫자열 리스트
    bj = list(map(int, input().split()))
    # bj : M개의 숫자로 구성된 숫자열 리스트

    # 모든 케이스에서 N이 더 큰 경우로 설정
    if M > N:
        M,N = N,M
        bj,ai = ai,bj

    # 긴 배열에서 짧은 배열만큼 뽑은 수를 담을 2차원 배열
    matrix = [[0] * N for _ in range(N - M + 1)]
    result = 0
    for i in range(N-M+1):
        # i : bj 길이만큼의 인덱스
        # print(i) i = 0,1,2
        # aj[i] => bj길이만큼 aj 원소
        tmp = 0
        for j in range(M):
            # j : matrix에서 aj가 들어갈 인덱스
            # print(j)
            tmp += (ai[i+j] * bj[j])
            print(ai[i+j], end=' ')

        # print(tmp)
        if result < tmp:
            result = tmp
        print(result)
            # matrix[i][j] += ai[j]
    # print(matrix)













    # matrix = [[0]*N for _ in range(N-M+1)]
    # # 길이가 짧은 bj가 입력될 길이가 더 긴 리스트의 길이의 1차원 배열
    # for i in range(N-M+1):
    #     # i : matrix에서 bj가 처음 입력될수 있는 인덱스
    #     # (N-M+1) : M길이 만큼 남아있어야함
    #     for j in range(i, i+M):
    #         # j : bj의 인덱스
    #         matrix[i][j] += bj[j]
    # print(matrix)