import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [[0]*10 for _ in range(10)] # 10*10 배열

    result = 0 # 보라색 개수
    for i in range(N):
        r1, c1, r2, c2, c = list(map(int, input().split()))
        for x in range(r1, r2+1):           # 행 길이
            # print(x)                      # 2, 3, 4
            for y in range(c1, c2+1):       # 열 길이
                # print(y)                  # 2, 3, 4
                matrix[x][y] += c

                if matrix[x][y] == 3:   # 3이 되면 보라색
                    result += 1         # 보라색 개수 +1
    print(result)

