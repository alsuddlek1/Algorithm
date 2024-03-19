import sys
input = sys.stdin.readline

def DFS(y, x):
    global idx # idx = 1 이면 1단지
    stack = [(y,x)] # data의 모든 집을 확인하면서 집이 있고, 아직 방문하지 않은 좌표 / 즉, 단지 시작 좌표
    visited[y][x] = idx # 방문한 곳을 단지로 수 변경
    cnt = 1 # 연결된 집의 개수
    while stack: # 스택에 값이 빌때까지
        sj, si = stack.pop() # 연결된 좌표
        # print(sj, si)
        di = [1, -1, 0, 0]
        dj = [0, 0, 1, -1]
        for d in range(4):
            nj = sj + dj[d]
            ni = si + di[d]
            if 0 <= ni < N and 0 <= nj < N:
                if data[nj][ni] == 1 and visited[nj][ni] == 0:
                    visited[nj][ni] = idx
                    cnt += 1
                    stack.append((nj, ni))
    idx += 1
    return cnt

# 입력값
N = int(input())
data = [list(map(int, input().rstrip())) for _ in range(N)]

# 방문 확인
visited = [[0]*N for _ in range(N)]

idx = 1 # 단지 번호
result = [] # 각 단지의 집의 개수 저장할 리스트

# data의 모든 집을 확인하면서 집이 있고, 아직 방문하지 않았다면 DFS를 호출하여 단지 찾기
for i in range(N):
    for j in range(N):
        if data[i][j] == 1 and not visited[i][j]:
            # 각 단지의 집의 개수를 result에 추가
            result.append(DFS(i,j))
# 오름차순 정렬(문제)
result.sort()

# 단지 개수
n = len(result)
print(n)

# 단지 별 집 개수
for i in range(n):
    print(result[i])