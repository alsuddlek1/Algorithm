## BOJ_16493_S3_최대페이지수
## https://www.acmicpc.net/problem/16493
## DP

n, m = map(int, input().split())
day = []
page = []
for i in range(m):
    d, p = map(int, input().split())
    day.append(d)
    page.append(p)

dp = [[0]*(n+1) for _ in range(m+1)]

for i in range(1, m+1):
    for j in range(n+1):
        dp[i][j] = dp[i-1][j]

        if j >= day[i-1]:
            dp[i][j] = max(dp[i][j], dp[i-1][j-day[i-1]] + page[i-1])

print(dp[m][n])