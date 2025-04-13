# DFS를 사용한 촌수 계산

# 전체 사람 수 입력
n = int(input())

# 촌수를 계산해야 할 두 사람 입력
a, b = map(int, input().split())

# 부모 자식 관계의 개수 입력
m = int(input())

# 인접 리스트를 이용해 그래프 초기화 (1번 사람부터 시작하므로 n+1)
graph = [[] for _ in range(n + 1)]

# 부모 자식 관계를 기반으로 양방향 그래프 생성
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)  # 양방향 그래프이므로 서로 연결

# 방문 여부를 저장할 리스트
visited = [False] * (n + 1)

# 결과 변수 (촌수 저장), 초기값은 -1
result = -1

def dfs(current, count):
    global result
    visited[current] = True  # 현재 노드 방문 처리

    # 목표 사람을 찾았을 경우
    if current == b:
        result = count  # 현재까지의 촌수를 결과에 저장
        return

    # 연결된 사람들 중 방문하지 않은 사람을 DFS로 탐색
    for neighbor in graph[current]:
        if not visited[neighbor]:
            dfs(neighbor, count + 1)  # 촌수 1 증가하며 재귀 호출

# DFS 시작 (a번 사람에서 시작)
dfs(a, 0)

# 결과 출력 (촌수를 못 찾으면 -1 그대로 출력됨)
print(result)
