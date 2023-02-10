import sys
sys.stdin = open('s_input.txt')

def solve(arr):
    for lst in arr:             # 행체크
        if len(set(lst)) != 9:  # 스도쿠 실패
            return 0

    # 열 list
    arr_t = list(zip(*arr))
    for lst in arr_t:           # 열체크
        if len(set(lst)) != 9:   # 스도쿠 실패
            return 0

    # 3*3 격자
    for i in (0, 3, 6):
        for j in (0, 3, 6):
            lst = arr[i][j:j+3] + arr[i+1][j:j+3] + arr[i+2][j:j+3] # 3*3 리스트
            # print(lst)
            if len(set(lst)) != 9: # 스도쿠 실패!!
                return 0

    return 1

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int,input().split()))for _ in range(9)]
    ans = solve(arr)

    print(f'#{tc} {ans}')