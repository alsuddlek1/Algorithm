import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):

            print(data[i][N//2])