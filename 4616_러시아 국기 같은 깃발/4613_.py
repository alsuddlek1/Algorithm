import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    data = [list(input()) for _ in range(4)]

    for i in range(N):
        for j in range(M):
            if data[0][]