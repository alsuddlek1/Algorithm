N = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
sum = 0
for i in range(N):
    sum += data[i]
    result = result + sum

print(result)