N = int(input())
data = list(map(int, input().split()))

set_data = []
for i in range(N):
    if data[i] not in set_data:
        set_data.append(data[i])

set_data.sort()

print(*set_data)