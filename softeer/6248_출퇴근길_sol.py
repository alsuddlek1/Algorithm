import sys
input = sys.stdin.readline
# 재귀를 사용할 경우 꼭 적어주자! : 백준의 경우 깊이가 10**3 이라 문제가 없었지만, 소프티어는 조건이 100000 이기 때문
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
adjR = [[] for _ in range(n+1)]

for _ in range(m): # 간선의 개수
    x, y = map(int, input().split())
    adj[x].append(y)
    adjR[y].append(x)

s,t = map(int, input().split())

def DFS(now, adj, visited):
    if visited[now] == 1:
        return
    visited[now] = 1
    for neighbor in adj[now]:
        DFS(neighbor, adj, visited)
    return

fromS = [0]*(n+1)
fromS[t] = 1
DFS(s, adj, fromS)

fromT = [0]*(n+1)
fromT[s] = 1
DFS(t, adj, fromT)

toS = [0] * (n+1)
DFS(s,adjR, toS)

toT = [0] * (n+1)
DFS(t, adjR, toT)

count = 0
for i in range(1, n+1):
    if fromS[i] and fromT[i] and toS[i] and toT[i]:
        count += 1

print(count-2)
