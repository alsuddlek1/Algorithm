n, m = map(int, input().split())
data = [[0]*m for _ in range(n)]
c = 0
cnt = 0

for i in range(m-1, -1, -1):
    if cnt % 2 == 1:
        cnt += 1
        for j in range(n-1, -1, -1):
            c += 1
            data[j][i] = c
    else:
        cnt += 1
        for j in range(n):
            c += 1
            data[j][i] = c

for i in range(n):
    for j in range(m):
        print(data[i][j], end=" ")
    print()