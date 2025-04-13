# 0. 변수설정
n = int(input())
start, target = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

result = -1 # 촌수 못 찾았을 때 초기값

# 1. 양방향 그래프 생성
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x) # <- 양방향이라서 서로 연결

# 2. dfs
def dfs(current, count):
    global result
    visited[current] = True

    if current == target:
        result = count
        return

    for neighbor in graph[current]:
        if not visited[neighbor]:
            dfs(neighbor, count + 1)

dfs(start, 0)

### 결과
print(result)