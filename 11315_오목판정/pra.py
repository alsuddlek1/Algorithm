import sys
sys.stdin = open('sample_input.txt')

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = [list(input()) for _ in range(N)]


    for x in range(N):
        for y in range(N):
            if data[x][y] == 'o':
                data[x][y] = 1
            else:
                data[x][y] = 0
    # print(data)
                cnt = data[x][y]
                for i in range(4):
                    for j in range(1,N):
                        nx = x + dx[i]*j
                        ny = y + dy[i]*j
                        if 0 <= nx < N and 0 <= ny < N :
                            cnt += [nx][ny]
                if cnt >= 5:
                    print('yes')
                else:
                    print('no')
