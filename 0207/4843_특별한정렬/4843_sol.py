# 특별한 정렬

import sys
sys.stdin = open('sample_input.txt')
T = int(input())

# 선택정렬
def selectionSort(num, N):
    for i in range(N - 1):
        minIdx = i
        for j in range(i + 1, N):
            if num[minIdx] > num[j]:
                minIdx = j
        num[i], num[minIdx] = num[minIdx], num[i]  # 오름차순
    return num

for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))
    # result => [a[-1] a[0] a[-2] ....]
    num = selectionSort(num, N)
    result = []
    for x in range(N//2):
        a = num[-x-1]
        result.append(a)
        b = num[x]
        result.append(b)
    res = result[:10]

    print(f'#{tc}', *res)


