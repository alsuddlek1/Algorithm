# 0. 변수설정
n = int(input())
arr = list(map(int, input().split()))

# 1. 스택
stack = []
result = [0] * n
for i in range(n):
    while stack:
        if stack[-1][1] >= arr[i]:
            result[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append([i, arr[i]])

print(*result)