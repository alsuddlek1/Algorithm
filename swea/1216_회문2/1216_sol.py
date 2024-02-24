def is_pal(arr, leng):
    for lst in arr:
        for i in range(N - leng + 1):
            if lst[i:i+leng] == lst[i:i+leng][::-1]:
                return True
    return False

for tc in range(1, 11):
    TC = int(input())
    N = 100

    # 가로행렬
    arr1 = list(input() for _ in range(N))
    # 세로 전치행렬
    arr2 = [''.join(x) for x in zip(*arr1)]

    for leng in range(N, 1, -1): # 찾으면 최대값
        if is_pal(arr1, leng) or is_pal(arr2, leng):
            break
    print(f'#{tc} {leng}')