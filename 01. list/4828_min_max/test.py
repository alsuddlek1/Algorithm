import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    maxV = 0
    minV = 1000000
    for i in range(len(arr)):
        if maxV < arr[i]:
            maxV = arr[i]
    # print(maxV)

        if arr[i] < minV:
            minV = arr[i]
    # print(minV)

    result = maxV - minV
    print(f'#{tc} {result}')