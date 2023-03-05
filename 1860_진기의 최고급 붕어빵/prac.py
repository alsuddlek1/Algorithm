import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int,input().split())
    # N명의 사람, M초당 K개의 붕어빵
    data = list(map(int, input().split()))
    dataa = sorted(data)

    people = 0
    for i in dataa:
        people += 1
        bread = (i//M) * K

    if bread < people:
        print(f'#{tc}', 'impossible')
    else:
        print(f'#{tc}', 'possible')