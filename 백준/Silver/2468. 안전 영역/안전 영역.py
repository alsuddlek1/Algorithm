# 0. 변수설정
import copy

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
result = 1
cnt = 0

def in_range(x,y):
    return 0 <= x < N and 0 <= y < N

# 1. 높이 비교
def getHigh():
    s, e = 100, 0
    for i in range(N):
        for j in range(N):
            s = min(data[i][j], s)
            e = max(data[i][j], e)

    return s, e

s, e = getHigh()

# 2. 홍수 지역 설정
def setPlace(h):
    place = copy.deepcopy(data)

    for i in range(N):
        for j in range(N):
            if place[i][j] <= h:
                place[i][j] = -1

    return place

# 3. 안전한 구역 count
# place = setPlace(4)

def getPlace(x, y):
    stack = [(x, y)]

    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    while stack:
        cx, cy = stack.pop()
        for dx, dy in zip(dxs, dys):
            nx = cx + dx
            ny = cy + dy
            if in_range(nx,ny) and place[nx][ny] != -1:
                place[nx][ny] = -1
                stack.append((nx, ny))


# 2. 잠기는 비 양
for h in range(s, e+1):
    place = setPlace(h)
    cnt = 0
    for i in range(N):
        for j in range(N):
            if place[i][j] != -1:
                cnt += 1
                getPlace(i, j)

    result = max(result, cnt)

print(result)