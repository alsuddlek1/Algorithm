import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = float(input())

    # N = 0.625
    # 0.101 (이진수)
    # = 1*2-1 + 0*2-2 + 1*2-3
    # = 0.5 + 0 + 0.125
    # = 0.625

    result = ''
    while N:    # N이 값이 있는동안 : 0이면 멈춤
        N *= 2  # N에 2를 곱해서 N이 1보다 크거나 같으면 1 아닐 때 0
        if N >= 1:
            N -= 1
            result += '1'

        else:
            result += '0'
        # print(N)

    # N을 소수점 아래 12자리 이내인 이진수로 표시할 수 있으면 0.을 제외한 나머지 숫자를 출력하고, 13자리 이상이 필요한 경우에는 ‘overflow’를 출력
    if len(result) >= 13:
        print('overflow')
    else:
        print(result)
