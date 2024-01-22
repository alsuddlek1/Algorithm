N = int(input()) # 회의 수

data = [[0]*2 for _ in range(N)] # 회의 시간표
result = 1

for x in range(N):
    sta, end = map(int, input().split())
    data[x][0] = sta
    data[x][1] = end

# 회의가 끝나는 시간(x[1])을 기준으로 정렬 후 동시간일때 시작 시간이 더 빠른 기준
data.sort(key = lambda x: (x[1], x[0]))

# 가장 빨리 회의가 끝나는 시간 data[0][1]
end_time = data[0][1]
for i in range(1, N):
    # 시작시간이 끝나는 시간보다 늦거나 같을 때
    if data[i][0] >= end_time:
        result += 1
        end_time = data[i][1]

print(result)