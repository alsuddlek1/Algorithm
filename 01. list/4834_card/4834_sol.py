import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    a = list(map(int, input()))

    vv = [0] * 10    # 숫자 담을 공간
    max_count = 0   # 가장 많은 횟수
    max_value = 0   # 가장 큰 수
    for i in a:
        vv[i] += 1
        if max_count < vv[i]:
            max_count = vv[i]
            max_value = i
        elif max_count == vv[i] and max_value < i:
            max_count = vv[i]
            max_value = i

    print(f'#{tc} {max_value} {max_count}')


