n,m = map(int, input().split())
data = [[0] * m for _ in range(n)]
c = 0

for i in range(n):
    for j in range(m):
        if j < m-1:
            c += 1
            data[i][j] = c
        elif j == m-1:
            c += 1
            data


for i in range(n):
    for j in range(m):
        print(data[i][j], end=' ')
    print()