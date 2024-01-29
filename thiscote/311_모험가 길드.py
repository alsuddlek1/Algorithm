N = int(input())
data = list(map(int, input().split()))

data.sort()
print(data)
result = 0 # 최종 결과 그룹 수
cnt = 0 # 그룹 당 인원 수

# 공포도에 맞춰서 팀 인원짜면 출발
for i in range(N):
    cnt += 1
    # 그룹 당 인원 수가 공포도 수에 맞춰지면 조 편성(result)에 += 1
    if cnt >= data[i]:
        result += 1
        cnt = 0

print(result)
