import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for __ in range(N):
        print(arr[__])

    # 각 행에서 최소값
    minV_list = []
    for i in range(N):
        minV = 10
        for j in range(N):
            if arr[i][j] < minV:
                minV = arr[i][j]
        minV_list.append(minV)
    print(minV_list)

    # 최소값 중 최소값
    minV2 = 10
    minidx= 0
    for i in range(len(minV_list)):
        # print(i)
        if minV_list[i] < minV2:
            minV2 = minV_list[i]
            minidx = i
    print(minV2)
    print(minidx)

    # 최소값 중 최소값의 행을 제외하고 다시 최소값 찾기
    # for i in range(N):
    #     removed = arr.pop[minidx][minidx]
    #     print(removed)