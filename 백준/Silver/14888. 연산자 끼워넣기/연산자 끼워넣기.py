# 1. 변수설정
n = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_result = -float('inf')
min_result = float('inf')


# 2. 계산 dfs
def dfs(idx, current_result, add, sub, mul, div):
    global max_result, min_result
    if idx == n:
        max_result = max(max_result, current_result)
        min_result = min(min_result, current_result)
        return
    if add:
        dfs(idx + 1, current_result + numbers[idx], add - 1, sub, mul, div)
    if sub:
        dfs(idx + 1, current_result - numbers[idx], add, sub - 1, mul, div)
    if mul:
        dfs(idx + 1, current_result * numbers[idx], add, sub, mul - 1, div)
    if div:
        if current_result < 0:
            dfs(idx + 1, -(-current_result // numbers[idx]), add, sub, mul, div - 1)
        else:
            dfs(idx + 1, current_result // numbers[idx], add, sub, mul, div - 1)

# 3. dfs 호출
dfs(1, numbers[0], add, sub, mul, div)

print(max_result)
print(min_result)