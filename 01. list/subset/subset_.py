import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    a = []
    n = len(arr)

    for i in range(1, 1<<n):
        result = 0
        for j in range(n):
            if i & (1<<j):
                # print(arr[j], end = ", ")
                result += arr[j]
        a.append(result)
    for i in range(len(a)):
        if a[i] == 0:
            print(1)
            break
    else: # for 문 끝까지 돌면 감
        print(0)
    # print(a)