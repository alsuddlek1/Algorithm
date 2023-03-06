import sys
sys.stdin = open('sample_in.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    # 오름차순 정렬
    arr_ = sorted(arr)

    minV = 1000
    for i in range(N-2):
        # i : '소' 박스스
       for j in range(i+1, N-1):    # '중'박스
           if arr_[i] != arr_[i+1] and arr_[j] != arr_[j+1]:    # 같은 크기가 다른 박스에 들어가지 않기
               A = i+1  # 인덱스 기준으로 하나 더 많음
               B = j-i
               C = N-1-j
               if A*B*C != 0 and A <= N//2 and B <= N//2 and C <= N//2:     # 빈박스x, 초과박스 x
                   if minV > max(A, B, C) - min(A, B, C):
                       minV = max(A, B, C) - min(A, B, C)

    if minV == 1000: # 포장할 수 없는 경우
        minV = -1

    print(f'#{tc} {minV}')