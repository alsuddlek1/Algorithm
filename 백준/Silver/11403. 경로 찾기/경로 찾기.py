# 0. 변수설정
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
visited = [0] * n

# 1. dfs
def dfs(x):
    for i in range(n):
        if data[x][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i)

# 2. dfs 실행
for i in range(n):
    dfs(i)
    for j in range(n):
        print(visited[j], end=" ")
    print()
    
    visited = [0 for _ in range(n)]