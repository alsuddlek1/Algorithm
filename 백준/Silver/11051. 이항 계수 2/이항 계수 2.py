## 0. 변수 설정
n, k = map(int, input().split())
mod = 10007

dp = [[0] * (k+1) for _ in range(n+1)]

# 1. 이항계수
# n! / k!(n-k)!
for i in range(n+1):
    for j in range(min(i,k) +1):
        if j == 0 or j == i:
            dp[i][j] = 1
        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % mod

print(dp[n][k])