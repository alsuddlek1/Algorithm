import sys
sys.stdin = open('input.txt')

w, h = map(int, input().split())    # matrix 의 행, 열 크기
p, q = map(int, input().split())    # 개미 시작 위치
t = int(input())                    # 총 이동 시간(횟수)

matrix = [[0]*(w+1) for _ in range(h+1)]

for i in range(w+1):        # matrix의 행 인덱스
    for j in range(h+1):    # matrix의 열 인덱스
        matrix[q][p] = 1
