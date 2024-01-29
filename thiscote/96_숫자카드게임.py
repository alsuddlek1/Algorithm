N,M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

result = 0
for i in range(N):
    min = 10000
    for j in range(M):
        if data[i][j] <= min:
            min = data[i][j]
    if min >= result:
        result = min

print(result)