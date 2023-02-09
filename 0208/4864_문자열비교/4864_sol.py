import sys
sys.stdin = open('sample_input.txt')

T = int(input())


for tc in range(1,T+1):
    short = input()
    long = input()

    result = 0
    p_idx = 0
    t_idx = 0
    check_t_idx = t_idx
    while t_idx < len(long):
        if short[p_idx] == long[check_t_idx]:
            p_idx += 1
            check_t_idx += 1
            if p_idx == len(short):
                result = 1
                break
        else:
            p_idx = 0
            t_idx += 1
            check_t_idx = t_idx
    print(result)

    # if str1 in str2:
    #     print(f'#{tc} 1')
    # else:
    #     print(f'#{tc} 0')