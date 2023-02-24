import sys
sys.stdin = open('sample_input.txt')

# 부분집합의합이 k인 개수 출력
# 1~12에서 N개를 골라 합이 6이 되어야함

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(range(1, 13))
# arr에서 n개
    result = 0
    for i in range(1<<len(arr)):
        tmp = []
        for j in range(len(arr)):
            if i
