import sys
input = sys.stdin.readline

## 3. DFS
def DFS(x,y):
    global result
    stack = [(x,y)]
    # 방문한 곳을 result(몇단지인지) 값으로 변환
    visited[x][y] = result
    cnt = 1 # 단지 별 집이 몇 개 있는지
    while stack:
        sx, sy = stack.pop()
        dx = [-1, 1, 0, 0] # 상하좌우
        dy = [0, 0, -1, 1]
        for dir in range(4):
            nx = sx + dx[dir]
            ny = sy + dy[dir]
            if 0 <= nx < N and 0 <= ny < N:
                if data[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = result
                    cnt += 1
                    stack.append((nx, ny))
    result += 1
    return cnt

## 1. 입력 받기
N = int(input())
data = [list(map(int, input().rstrip())) for _ in range(N)]

visited = [[0]*N for _ in range(N)]
result = 1 # 단지 수
result_list = [] # 단지 수를 담은 리스트(나중에 sort해서 단지 내 집의 수 오름차순으로 정렬)

## 2. 배열 돌면서 집이 있고 방문하지 않았을 경우에 DFS
for i in range(N):
    for j in range(N):
        if data[i][j] == 1 and not visited[i][j]:
            result_list.append(DFS(i,j))

## 4. 출력
result_list.sort()
print(len(result_list))

for i in result_list:
    print(i)