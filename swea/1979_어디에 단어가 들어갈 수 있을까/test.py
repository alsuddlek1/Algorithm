import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N,K = map(int,input().split())
    # N : N*N 행렬의 크기
    # K : 단어의 길이
    matrix = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N-K+1):
            for k in range(j, j+K):
                print(k)
    print()