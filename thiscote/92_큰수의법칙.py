N, M, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)
result = K*(M//K)*data[0] + (M%K)*data[1]

print(result)


























# data.sort(reverse=True)
#
# result = 0
#
# while True:
#     for i in range(K):
#         if M == 0:
#             break
#         result += data[0]
#         M -= 1
#     if M == 0:
#         break
#     result += data[1]
#     M -= 1
#
# print(result)

