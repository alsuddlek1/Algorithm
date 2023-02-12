import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    pat = input()
    tar = input()
    p_idx = 0
    t_idx = 0
    cnt = 0
    while t_idx < len(tar):
        if pat[p_idx] != tar[t_idx]:
            p_idx = p_idx - t_idx
            t_idx = -1
        p_idx += 1
        t_idx += 1
        if p_idx == len(pat):
            cnt += 1
            p_idx = 0

    if cnt == 0:
        print(0)
    else :
        print(1)
