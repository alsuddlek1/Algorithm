import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input()))for _ in range(N)]
    for i in range(N):
        print(matrix[i])

