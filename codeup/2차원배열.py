n = int(input())

result = [[0]*(n+1) for _ in range(n+1)]
c = 1

for i in range(1, n+1):
    for j in range(n, 0, -1):
        print(i, j)
        result[i][j] = c
        print(result)
        c += 1

for x in range(1, n+1):
    for y in range(1, n+1):
        print(result[x][y], end=' ')
    print()