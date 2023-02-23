import sys
sys.stdin = open('input.txt')

def DFS(start):
    visited = [0] * 100
    stack = [start]

    while stack:
        start = stack.pop()
        if start == G:
            return 1
        if visited[start] == 0:
            visited[start] = 1
        for next in range(100):
            if matrix[start][next] and not visited[next]:
                visited[next] = 1
                stack.append(next)
    return 0

for tc in range(1, 11):
    tc, E = map(int, input().split())
    matrix = [[0]*100 for _ in range(100)]

    data = list(map(int, input().split()))
    for i in range(E):
        x,y = data[i*2],data[i*2+1]
        matrix[x][y] = 1

    S, G = 0, 99
    print(DFS(S))