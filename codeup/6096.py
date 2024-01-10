data = [list(map(int, input().split())) for _ in range(19)]

n = int(input())

for _ in range(n):
    x,y = map(int, input().split())
    for i in range(19):
        if data[x][i] == 0:
            data[x][i] = 1
        else:
            data[x][i] = 0
        for j in range(19):
            if data[j][y] == 0:
                data[j][y] = 1
            else:
                data[j][y] = 0

for i in range(19):
    for j in range(19):
        print(data[i][j], end= " ")
    print()

