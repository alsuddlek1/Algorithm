# N = int(input())
# data = list(map(int, input().split()))
#
# result = []
# max_value = 10000
#
# for i in range(N):
#     num = 0
#     for j in range(N):
#         num += abs(data[j] - data[i])
#     if max_value >= num:
#         max_value = num
#         result.append(data[i])
#
# print(min(result))

N = int(input())
data = list(map(int, input().split()))
data.sort()

median = data[N // 2]
print(median)

result = []
num = 0
for x in data:
    num += abs(x-median)
    result.append(x)

print(result)
