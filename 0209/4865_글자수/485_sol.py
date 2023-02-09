import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    cnts = []
    for i in str1:
        cnt = 0
        # print(cnt)
        for j in str2:
            if i == j:
                cnt += 1
                print(cnt)
        cnts.append(cnt)
    # print(max(cnts))