import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    NM = list(map(int,input().split()))
    N = NM[0]
    M = NM[1]
    arr = list(map(int, input().split()))

    init = 0
    for i in range(M): # M개의 이웃한 수의 합
        init += arr[i]
        # print(init)

    maxV = minV = init
    for i in range(N-M+1):
        tmp = 0
        for j in range(i, i+M):
            # print(j) # 012, 123, 234,,,,
            tmp += arr[j]

    if tmp > maxV:
        maxV = tmp
    if tmp < minV:
        minV = tmp

    result = maxV - minV

    # print(f'#{tc} {result}')
