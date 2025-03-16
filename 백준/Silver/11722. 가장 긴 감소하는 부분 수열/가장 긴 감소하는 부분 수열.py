# 0. 변수설정
n = int(input())
arr = list(map(int, input().split()))
result = 0
dp = [1] * n

# 1. 부분수열 감소 판단
for i in range(1, n):
    for j in range(i):
        if arr[i] < arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))