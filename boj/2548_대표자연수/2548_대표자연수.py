## 반복문을 활용한 풀이
import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))

result = []
max_value = 10000

for i in range(N):
    num = 0
    for j in range(N):
        num += abs(data[j] - data[i])
    if max_value >= num:
        max_value = num
        result.append(data[i])

print(min(result))


## 중앙값을 이용한 풀이
import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))
data.sort()

median = data[N // 2]

num = 0
for x in data:
    num += abs(x-median)

for i in range(N):
    cnt = 0
    for j in range(N):
        cnt += abs(data[j] - data[i])
    if cnt == num:
        print(data[i])
        break