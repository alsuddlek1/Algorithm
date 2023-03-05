import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int,input().split())
    # N명의 사람, M초당 K개의 붕어빵
    data = list(map(int, input().split()))
    dataa = sorted(data) # 사람들 방문하는 시간 정렬

    result = 'Possible'
    people = 0 # 한명당 붕어빵 하나씩 줘야함
    for i in dataa:
        people += 1
        bread = (i//M) * K

        if people > bread:
            result = 'Impossible'
            break
    print(f'#{tc} {result}')