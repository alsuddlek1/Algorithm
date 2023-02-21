import sys
sys.stdin = open('sample_input.txt')
from collections import deque

def BFS(data, S, V):
    visited = [0] * (V+1)
    queue = deque([])
    queue.append(S)
    visited[S] = 1  # S가 스타트점

    while queue:
        t = queue.popleft()
        if t == G:
            return visited[t] - 1

        for i in range(len(data[t])):
            if data[t][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = visited[t] + 1
    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    data = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        x,y = map(int, input().split())
        data[x][y] = 1
        data[y][x] = 1
    S, G = map(int,input().split())

    print(f'#{tc}', BFS(data,S,V))