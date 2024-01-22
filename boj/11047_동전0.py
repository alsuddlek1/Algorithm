N, K = map(int, input().split())
coin_types = []
result = 0

for _ in range(N):
    A = int(input())
    coin_types.append(A)

coin_types.sort(reverse=True)

for i in coin_types:
    result += K // i
    K %= i

print(result)