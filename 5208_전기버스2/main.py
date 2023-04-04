import sys
sys.stdin = open('sample_input.txt')

def aa(i, tmp):
    global cnt
    if i == N:
        cnt = min(tmp, cnt)
        return
    if tmp > cnt:
        return

    elif i < N:
        for _ in range(M[i]):
            i += 1
            tmp += 1
            aa(i, tmp)
            tmp -= 1

T = int(input())
for tc in range(1, T+1):
    N, *M = list(map(int, input().split()))
    N = N-1

    result = M[]