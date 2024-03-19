import sys

input = sys.stdin.readline

N, K = map(int, input().split())
data = list(map(int, input().split()))

for i in range(K):
    avg_list = []
    s, e = map(int, input().split())
    for i in range(s - 1, e):
        avg_list.append(data[i])

    avg = sum(avg_list) / len(avg_list)
    result = format(round(avg, 2), ".2f")
    print(result)
