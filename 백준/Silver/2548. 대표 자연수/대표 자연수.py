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