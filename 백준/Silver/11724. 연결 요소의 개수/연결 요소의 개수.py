## 00. 재귀 깊이 제한
import sys
sys.setrecursionlimit(10**5)

# 0. 변수 설정
N, M = map(int, input().split())

# 2. dfs
visited = [False] * (N+1)
def dfs(i):
    visited[i] = True
    for n in graph[i]:
        if not visited[n]:
            dfs(n)

# 1. dfs 판단 할 그래프
graph = [[] for _ in range(N+1)]
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 3. dfs호출
result = 0
for i in range(1, N+1):
    if not visited[i]:
        result += 1
        dfs(i)

print(result)