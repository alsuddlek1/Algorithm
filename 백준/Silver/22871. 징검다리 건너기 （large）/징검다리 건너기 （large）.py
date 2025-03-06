# 0. 변수설정
N = int(input())
arr = list(map(int, input().split()))

# 1. dp 설정
dp = [1000000 for _ in range(N)]
dp[0] = 0

# 2. 징검다리 건너기
for i in range(1,N):
    for j in range(i):
        power = max((i-j) * (1+abs(arr[j]-arr[i])), dp[j])
        dp[i] = min(dp[i], power)

print(dp[-1])
