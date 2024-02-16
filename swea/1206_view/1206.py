for _ in range(10):
    N = int(input())
    data = list(map(int, input().split()))
    result = 0

    for i in range(2, N-2):
        floor = data[i]
        for j in range(i-2, i+3):
            if i == j:
                continue
            if data[i] > data[j]:
                apt = data[i] - data[j]
                if apt < floor:
                    floor = data[i] - data[j]
            elif data[i] <= data[j]:
                break
        else:
            result += floor

    print(f'#{_+1} {result}')