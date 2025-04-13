def dfs(current, depth):
    visited[current] = True
    if current == target:
        print(depth)
        exit()
    for neighbor in graph[current]:
        if not visited[neighbor]:
            dfs(neighbor, depth + 1)

n = int(input())
start, target = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n + 1)
dfs(start, 0)
print(-1)
