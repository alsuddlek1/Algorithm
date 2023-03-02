import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N,K = map(int,input().split())
    # N : N*N 행렬의 크기
    # K : 단어의 길이
    matrix = [list(map(int, input().split())) for _ in range(N)]


    cnt = 0
    for x in range(N): # x : data의 행 인덱스
        # cnt = 0
        for i in range(N-K+1): # i : k길이 제외한 data의 열 인덱스
            # print(i) # i = 0,1,2
            jj = [] # 값이 1인 j를 담을 리스트
            for j in range(i, i+K): # j : K개만큼의 인덱스
                # print(j)
                jj.append(matrix[x][j])
            print(jj)
            if jj == [1]*K: # jj = [1, 1, 1] 일때 cnt += 1
                cnt += 1
    print(cnt)
