# 0. 변수설정
N = int(input())
data = input()
INF = float('inf') # 무한대값 설정

# 1. B - O - J 순서대로 건너기
## 에너지 양 k**2
def setJump(N, data):
    dp = [INF] * N
    dp[0] = 0

    for i in range(N):
        for j in range(i+1, N):
            if data[i] == "B" and data[j] == "O":
                dp[j] = min(dp[j], dp[i] + (j-i)**2)
            elif data[i] == "O" and data[j] == "J":
                dp[j] = min(dp[j], dp[i] + (j - i) ** 2)
            elif data[i] == "J" and data[j] == "B":
                dp[j] = min(dp[j], dp[i] + (j - i) ** 2)

    if dp[N-1] == INF:
        return -1
    else:
        return dp[N-1]


result = setJump(N, data)
print(result)