import sys
sys.stdin = open('sample_input.txt')

## 그룹 나누기
def mergesort(arr):
    # 그룹이 하나 나왔을때 리스트로 나오면 크기비교 안되니까 숫자로받기
    if len(arr) <= 1:
        return arr[0]

    # 두개면 이때 가위바위보 ㄱㄱ
    if len(arr) <= 2:
        return rsp(arr)

    # 홀수, 짝수 경우 나누기
    if len(arr) % 2:
        arr_n = len(arr) // 2 + 1

    else:
        arr_n = len(arr) // 2

    arr_left = mergesort(arr[:arr_n])
    arr_right = mergesort(arr[arr_n:])
    arr_m = [arr_left, arr_right]

    return rsp(arr_m)

# 가위(1) 바위(2) => 2
# 바위(2) 보(3) => 3
# 보(3) 가위(1) => 1

## 가위 바위 보 ~~
def rsp(arr_m):
    global idx
    for i in range(len(arr_m)):
        # 가위일때
        if arr_m[i][0] == 1:
            if arr_m[i+1][0] == 1:
                idx = i
                return arr_m[i]
            elif arr_m[i+1][0] == 2:
                idx = i + 1
                return arr_m[i+1]
            elif arr_m[i+1][0] == 3:
                idx = i
                return arr_m[i]

        # 바위일때
        if arr_m[i][0] == 2:
            if arr_m[i+1][0] == 2:
                idx = i
                return arr_m[i]
            elif arr_m[i+1][0] == 3:
                idx = i + 1
                return arr_m[i+1]
            elif arr_m[i+1][0] == 1:
                idx = i
                return arr_m[i]

        # 묵일때
        if arr_m[i][0] == 3:
            if arr_m[i+1][0] == 3:
                idx = i
                return arr_m[i]
            elif arr_m[i+1][0] == 2:
                idx = i
                return arr_m[i]
            elif arr_m[i+1][0] == 1:
                idx = i + 1
                return arr_m[i+1]

T= int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = list(map(int, input().split()))
    for i in range(N):
        arr[i] = [arr[i], i+1]
    idx = 0
    print(f'#{tc} {mergesort(arr)[1]}')
