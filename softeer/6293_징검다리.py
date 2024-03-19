import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))

result = [1] * N

for i in range(1, N):
    cnt = 0
    for j in range(i):
        if data[i] > data[j]:
            if cnt < result[j]:
                cnt = result[j]

    result[i] = cnt + 1

print(max(result))
