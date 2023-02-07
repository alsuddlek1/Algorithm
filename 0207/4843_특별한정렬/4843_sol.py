# 특별한 정렬

import sys
sys.stdin = open('sample_input.txt')
T = int(input())

# 선택정렬 / 오름차순
def selectionSort(num, N): # N개의 정수
    for i in range(N - 1):
        minIdx = i
        for j in range(i + 1, N):
            if num[minIdx] > num[j]:
                minIdx = j
        num[i], num[minIdx] = num[minIdx], num[i] #
    return num

for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))
    num = selectionSort(num, N) # 오름차순으로 정렬된리스트
    result = [] # result => [a[-1] a[0] a[-2] ....]
    for x in range(N//2): # 개수가 10개 일때 큰수 -> 작은수 5개. 작은수 -> 큰수 5개
        a = num[-x-1] # 정렬된 리스트에서 마지막 인덱스가 가장 큰수
        result.append(a)
        b = num[x] # 정렬된 리스트에서 가장 작은수
        result.append(b)
        # append를 이용해 a,b를 순서대로 넣어줌
    res = result[:10] # 10개까지 출력

    print(f'#{tc}', *res)


