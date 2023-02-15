import sys
sys.stdin = open('input.txt')

def DFS(start):
    # 첫 시작위치아무튼 방문함
    visited[start] = 1
    stack = [start]
    while stack:
        start = stack.pop()
        # print(stack)
        # print(start, end=' ')
        if start == G: # 현재 조사 대상이 도착지점이면 조사 멈춰~~!!
            return 1

        for next in range(1, 100):
            if data[start][next] and not visited[next]:
                visited[next] = 1
                stack.append(next)
    return 0


for tc in range(10):
    tc, E = map(int,input().split())
    route = list(map(int, input().split()))

    data = [[0]*100 for _ in range(100)]
    visited = [0] * 100

    for i in range(0, len(route)-1, 2):
        # print(route[i])
        data[route[i]][route[i+1]] = 1

    S, G = 0, 99
    print(f'#{tc}', DFS(S))