import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))

    init = 0
    for i in range(M):
        init += arr[i]

    maxV = minV = init

    for i in range(N-M+1):
        tmp = 0
        for j in range(i, i+M):
            tmp += arr[j]

    if tmp > maxV:
        maxV = tmp
    if tmp < minV:
        minV = tmp

    result = maxV - minV

    print(f'#{tc} {result}')