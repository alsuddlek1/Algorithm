def is_pal_idx(arr, leng):
    for lst in arr:
        for i in range(N - leng + 1):
            for j in range(leng//2): # 몇개를 검사할지
                if lst[i+j] != lst[i+leng-1-j]:
                    break
            else:
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
        if is_pal_idx(arr1, leng) or is_pal_idx(arr2, leng):
            break
    print(f'#{tc} {leng}')