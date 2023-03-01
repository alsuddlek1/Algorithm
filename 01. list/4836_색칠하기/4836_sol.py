import sys
sys.stdin = open('input.txt')

# 보라색이 된 칸수 출력

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # N : 색칠할 영역의 개수(빨강/파랑 총 색칠 횟수)
    matrix = [[0] * 10 for _ in range(10)]
    # 색칠할 10*10 도화지 (인덱스 0부터 시작)
    result = 0
    # 보라색 개수
    for _ in range(N):
        r1, c1, r2, c2, c = map(int, input().split())
        # (r1, c1) : 왼쪽 위 모서리 '인덱스'
        # (r2, c2) : 오른쪽 아래 모서리 '인덱스'
        # c : 생상 정보 = 1 : 빨강, = 2 : 파랑 => 1+2=3 : 보라

        for x in range(r1, r2+1):
            # x : 색칠한 곳의 행 인덱스
            # (r1, r2+1) : r1부터 r2인덱스 까지 색칠
            for y in range(c1, c2+1):
                # y : 색칠한 곳의 열 인덱스
                # (c1, c2+1) : c1부터 c2인덱스 까지 색칠
                matrix[x][y] += c
                # x,y가 해당된 범위 안을 c(색상) 입력
                if matrix[x][y] == 3:
                    # 빨강 + 파랑 = 보라
                    # 1 + 2 = 3
                    # 보라색 카운트 +1
                    result += 1
    print(f'#{tc} {result}')

