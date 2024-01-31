N, M = map(int, input().split())
data = list(map(int, input().split()))

result = 0

for i in range(N):
    for j in range(i+1, N):
        if data[i] != data[j]:
            result += 1

print(result)