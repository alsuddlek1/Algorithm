import sys
sys.stdin = open('sample_input.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = str(N)
    matrix = [0]*10 # 0부터 9까지 등장 횟수 셀 배열

    cnt = 1 # 9까지 숫자 다 나올때까지
    while 0 in matrix: # matrix에 0 없을때까지
        i = str(cnt*N)
        for j in range(len(i)):
            matrix[int(i[j])] += 1
        cnt += 1
    print(f'#{tc}',int(i))