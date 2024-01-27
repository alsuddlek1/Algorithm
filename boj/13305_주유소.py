N = int(input())
road = list(map(int, input().split()))
cost = list(map(int, input().split()))

result = 0
M = cost[0]
for i in range(N-1):
    if cost[i] < M:
        M = cost[i]
    result += M * road[i]

print(result)