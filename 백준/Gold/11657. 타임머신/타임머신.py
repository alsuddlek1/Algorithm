INF = int(1e9)
N, M = map(int, input().split())
edges = []

for m in range(M):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

# 거리 배열 초기화
dist = [INF] * (N+1)
dist[1] = 0 # 시작점 : 1

# 1. 벨만-포드 : N-1번 반복
for i in range(N-1):
    for u, v, w in edges:
        if dist[u] != INF and dist[v] > dist[u] + w:
            dist[v] = dist[u] + w

# 2. 음수 사이클 검사
has_cycle = False
for u, v, w in edges:
    if dist[u] != INF and dist[v] > dist[u] + w:
        has_cycle = True
        break

## 결과
if has_cycle:
    print(-1)
else:
    for i in range(2, N+1):
        if dist[i] != INF:
            print(dist[i])
        else:
            print(-1)