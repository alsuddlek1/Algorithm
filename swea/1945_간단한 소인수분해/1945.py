T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num_list = [2, 3, 5, 7, 11]
    result = [0]*5

    for i in range(5):
        # print(num_list[i])
        while N % num_list[i] == 0:
            N //= num_list[i]
            result[i] += 1
    print(f'#{tc}', *result)