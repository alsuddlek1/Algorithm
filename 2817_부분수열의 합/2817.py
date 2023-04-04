import sys
sys.stdin = open('sample_input.txt')

def aa(i, res):
    global result
    if i == N:
        if res == K:
            result += 1
        return

    if res > K:
        return

    aa(i+1, res)
    aa(i+1, res + A[i])

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    result = 0
    aa(0, 0)
    print(result)