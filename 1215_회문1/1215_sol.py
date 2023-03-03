import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    data = [list(input()) for _ in range(8)]

    cnt = 0
    for i in range(8):
        for j in range(8-N+1):
            word = []
            for l in range(j, j+N):
                word.append(data[i][l])
                words = word
            words.reverse()
            # print(words)
            if word == words:
                cnt += 1
    print(cnt)