import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    pattern = input()
    target = input()
    cnt = 0
    p_idx = 0
    t_idx = 0
    while t_idx < len(target):
        if target[t_idx] != pattern[p_idx]:
            t_idx = t_idx - p_idx
            p_idx = -1
        p_idx += 1
        t_idx += 1

        if p_idx == len(pattern):
            cnt += 1
            p_idx = 0

    if cnt == 0:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} 1')
