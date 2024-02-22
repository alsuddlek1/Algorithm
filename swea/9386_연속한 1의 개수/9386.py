T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = input()
    result = 0
    result_arr = [0]*N

    for i in range(N):
        if data[i] == "1":
            result += 1
            result_arr[i] += result
        else:
            result = 0
    print(f'#{tc}', max(result_arr))