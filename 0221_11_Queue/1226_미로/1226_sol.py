import sys
sys.stdin = open('input.txt')
from collections import deque

# 시작점에서 끝점까지 길찾아가기

# 3. 길찾아야하니까 delta 쓰기

# 2. 시작점, 끝점까지 경로 찾기 0일때 이동 1일때 이동 불가능
# 줄 전체 조사 할거니까 BFS
def BFS(data, S):
    visited = [0] * 16
    queue = deque([])
    queue.append(S)
    visited[S] = 1

    while queue:
        t = queue.popleft()
        if t == 3:
            return 1
        for i in range(len(arr[t])):
            if arr[t][i] == 0 and visited[i] == 0:
                queue.append(i)
                visited[i] = visited[t] + 1
    return 0


    pass

# 1. 데이터 받기
for tc in range(10):
    tc = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    for x in range(16):
        for y in range(16):
            arr[x][y] = 1
    S = 0
    if arr[x][y] == 2:
        arr[x][y] = S


    print(BFS(arr,S))


