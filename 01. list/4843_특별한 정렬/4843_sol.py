import sys
sys.stdin = open('input.txt')

T = int(input())

# 선택정렬
def selectionSort(num, N):
    for i in range(N-1):
        minidx = i
        for j in range(i+1, N):
            if num[minidx] > num[j]:
                minidx = j
        num[i], num[minidx] = num[minidx], num[i]
    return num

for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))
    num = selectionSort(num, N)
    result = []
    for x in range(N//2):
        a = num[-x-1]
        result.append(a)
        b = num[x]
        result.append(b)
    # print(result)
    res = result[:10]

    print(f'#{tc}', *res)
