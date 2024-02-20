T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [0]*5001
    for i in range(N):
        A, B = map(int, input().split())
        for x in range(A, B+1):
            data[x] += 1

    P = int(input())
    result = [0]*(P+1)
    for i in range(1, P+1):
        C = int(input())
        result[i] = data[C]
    print(f'#{tc}', *result[1:])