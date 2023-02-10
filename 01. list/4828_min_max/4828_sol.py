import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    maxV = 0
    minV = 10000000

    for i in range(len(arr)):

        if arr[i] > maxV:
            maxV = arr[i]
        if arr[i] < minV:
            minV = arr[i]

    result = maxV - minV
    print(f'#{T} {result}')