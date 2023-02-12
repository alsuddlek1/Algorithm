import sys
sys.stdin = open('input.txt')

T = int(input())

def check():
    for i in range(N):
        for j in range(N-M+1):
            char = chars[i][j:j+M]
            if char == char[::-1]:
                return ''.join(char)

for tc in range(1,T+1):
    N, M = map(int,input().split())
    chars = [list(input()) for _ in range(N)]
    result = ''
    tmp = check()
    if tmp:
        result = tmp

    # 전치행렬
    for i in range(N):
        for j in range(N):
            if i < j:
                chars[i][j], chars[j][i] = chars[j][i], chars[i][j]

    tmp = check()
    if tmp:
        result = tmp


    print(f'#{tc} {result}')