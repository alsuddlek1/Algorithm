# 0. 변수설정
data = [list(map(int, input().split())) for _ in range(5)]
nums = []

# 1. dfs
def in_range(x, y):
    return 0 <= x < 5 and 0 <= y < 5

def dfs(x, y, lis):
    # print(lis)
    if len(lis) == 6:
        if lis not in nums:
            nums.append(lis)
            # print(nums)
        return

    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if in_range(nx, ny):
            dfs(nx, ny, lis + [data[nx][ny]])

# 2. dfs 실행
for i in range(5):
    for j in range(5):
        dfs(i, j, [data[i][j]])

print(len(nums))

