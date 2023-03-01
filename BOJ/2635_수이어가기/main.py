import sys
sys.stdin = open('input.txt')

## 가장 긴 길이의 리스트

N = int(input())

A = [] # 규칙을 담을 리스트
for i in range(1, N+1):
    # i : 1부터 N가지의 모든 수
    A = []
    A.append(i)

    len_A = 0
    AA = A[-2] - A[-1]
    while AA <= 0:
        A.append(AA)
        len_A += 1