import sys

# M = 가방의 무게 N = 귀금속 종류 수
M, N = map(int, input().split())
data = [[0] * 2 for _ in range(N)]
result = 0

for i in range(N):
    # M1 = 금속의 무게 P1=  무게당 가격
    M1, P1 = map(int, input().split())
    data[i][0] = M1
    data[i][1] = P1

data.sort(key=lambda x: x[1], reverse=True)

for i in range(N):
    if M >= data[i][0]:
        M -= data[i][0]
        result += data[i][0] * data[i][1]
    else:
        result += M * data[i][1]
        break

print(result)
