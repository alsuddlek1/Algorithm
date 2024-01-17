N = int(input())
data = list(map(int, input().split()))

sum = 0
result = []

for i in range(N):
    sum += data[i]
    result.append(sum)

print(*result)