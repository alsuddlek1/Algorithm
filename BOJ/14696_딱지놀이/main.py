import sys
sys.stdin = open('input.txt')

T = int(input()) # 딱지놀이의 총 라운드 수
for tc in range(1, T+1):
    A = list(map(int, input().split()))
    # A : A어린이가 낸 카드 : A[i*2] 모양의 개수, A[i*2+1]모양 순서
    B = list(map(int, input().split()))
    # B " B어린이가 낸 카드 : 모양의 개수, 모양 순서

    # 1. 딱지 모양 개수 비교
    # A의 딱지 모양 조서
    for i in range(len(A)-):
        # i : A의 인덱스
        Acard = 0
        if A[i*2+1]


