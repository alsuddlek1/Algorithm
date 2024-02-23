T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    cnt = 1
    result = [0] * N

    for i in range(N-1):
        if data[i] < data[i+1]:
            cnt += 1
            result[i] += cnt
        else:
            cnt = 1
            result[i] = 1
    print(f'#{tc}', max(result))
