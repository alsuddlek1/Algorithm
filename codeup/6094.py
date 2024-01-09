n = int(input())
data = list(map(int, input().split()))

result = 10000

for i in range(n):
    if result >= data[i]:
        result = data[i]
print(result)