import sys
sys.stdin = open('input.txt')

# 1. 데이터 받기
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
# 2. 연속된 M개의 수 합
# 인덱스값 M개 구하기
    idx = []
    for i in range(N-M):
        for j in range(i,M):
            # print(j)
            idx.append(j)
        print(idx)
# 3, max, min 구하고 result