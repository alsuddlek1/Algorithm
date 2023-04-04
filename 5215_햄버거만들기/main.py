import sys
sys.stdin = open('sample_input.txt')

def aa(i, sum_s, sum_k):
    global max_v
    if i == N:
        if sum_k <= L:
            if max_v <= sum_s:
                max_v = sum_s
        return

    if sum_k > L:
        return

    aa(i+1, sum_s, sum_k)
    aa(i+1, sum_s + S[i], sum_k + K[i])

T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    S = []
    K = []
    for _ in range(N):
        s, k = map(int, input().split())
        S.append(s)
        K.append(k)

    max_v = 0
    aa(0, 0, 0)
    print(max_v)