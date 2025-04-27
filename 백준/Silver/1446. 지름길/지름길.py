# 0. 변수 설정
N, D = map(int, input().split())
dp = [_ for _ in range(D + 1)]

line = []

for n in range(1, N+1):
    s, e, l = map(int, input().split())

    # 1. 고속도로 길이 내에 있는 길
    if e <= D:
        line.append((s, e, l))

line.sort()

idx = 0
for i in range(D+1):
    if i> 0:
        dp[i] = min(dp[i], dp[i-1] + 1)

    # 3. 지름길 확인
    while idx < len(line) and line[idx][0] == i:
        s, e, l = line[idx]
        if dp[e] > dp[s] + l:
            dp[e] = dp[s] + l
        idx += 1

print(dp[D])
