n, m = map(int, input().split())
result = [[0]*(m) for _ in range(n)]

c = 1

for i in range(m-1, -1, -1):
    for j in range(n):
        result[j][i] = c
        c += 1

for x in range(n):
    for y in range(m):
        print(result[x][y], end=" ")
    print()