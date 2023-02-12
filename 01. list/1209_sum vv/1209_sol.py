import sys
sys.stdin = open('input.txt')

for tc in range(10):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(100)]

    result = 0

    # 행우선 
    for i in range(100):
        a = 0
        for j in range(100):
            a += arr[i][j]
        if result < a:
            result = a
    # print(result)

    # 열우선
    for i in range(100):
        a = 0
        for j in range(100):
            a += arr[j][i]
        if result < a:
            result = a
    # print(result)

    # 대각선 l -> r
    for i in range(100):
        a = 0
        a += arr[i][i]
    if result < a:
        result = a
    # print(result)
    
    # 대각선 r->l
    for i in range(100):
        a = 0
        a += arr[i][99-i]
    if result < a:
        result = a
    # print(result)
            

    print(f'#{N} {result}')
