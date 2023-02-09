import sys
sys.stdin = open('sample_input.txt', encoding='utf-8')

T = int(input())

for tc in range(1,T+1):
    arr = list(input().split())
    A = arr[0]          #전체 텍스트
    B = arr[1]          # 패턴
    count = 0

    # for t_idx in range(len(A) - len(A)+1):
    #     for p_idx in range(len(A)):
    #         if A[p_idx] != B[t_idx + p_idx]:
    #             break
    #     else:
    #         count += 1
    # print(f'#{tc} {count}')

def BruteForce(B, A):
    A_idx = 0 # 전체 텍스트의 인덱스
    B_idx = 0 # 패턴의 인덱스
    while B_idx < len(B) and A_idx < len(A):
        if A[A_idx] != B[B_idx]:
            A_idx = A_idx - B_idx
            B_idx = -1
        A_idx = A_idx +1
        B_idx = B_idx +1
    if B_idx == len(B):
        return A_idx - len(A)
    else:
        return -1

print(BruteForce(B,A))