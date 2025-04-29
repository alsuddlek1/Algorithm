data = [list(map(int, input().split())) for _ in range(5)]
nums = []

## dfs
def in_range(x, y):
    return 0 <= x < 5 and 0 <= y < 5

def dfs(x, y, arr):
    if len(arr) == 6:
        if arr not in nums:
            nums.append(arr)
        return

    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if in_range(nx, ny):
            dfs(nx, ny, arr + [data[nx][ny]])

    return x, y

## dfs 실행
for i in range(5):
    for j in range(5):
        dfs(i, j, [data[i][j]])

## 정답
print(len(nums))