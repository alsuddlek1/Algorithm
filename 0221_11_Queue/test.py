import sys
sys.stdin = open('input.txt')

def BFS(noe):
    queue = [now]
    int(now, end=' ')
    # 방문표시 먼저 진행
    visited[now] = 1

    while queue:
        now = queue.pop()
        for next in range(1, V+1):
            # 만약
            if G[now][next] == 1 and visited[next]:
                queue.append(next)
                visited[next] = 1
                print(next, end=' ')

V, E = map(int, input().split())
temp = list(map(int, input().split()))

G = {key: [] for key in range(V+1)}
print(G)

for i in range(E):
    n1, n2 = temp[i*2], temp[i*2+1]
    G[n1].append(n2)
    G[n2].append(n1)