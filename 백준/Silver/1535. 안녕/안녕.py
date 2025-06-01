N = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))

dp = [0] * 101

for i in range(N):
    for j in range(100, L[i], -1):
        dp[j] = max(dp[j], dp[j - L[i]] + J[i])

print(max(dp))