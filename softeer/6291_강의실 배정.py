import sys
input = sys.stdin.readline

N = int(input())
schedule = [[0]*2 for _ in range(N)]
result = 1

for i in range(N):
    start, end = map(int, input().split())
    schedule[i][0] = start
    schedule[i][1] = end

schedule.sort(key = lambda x : (x[1], x[0]))

end_time = schedule[0][1]
for i in range(1, N):
    if schedule[i][0] >= end_time:
        result += 1
        end_time = schedule[i][1]

print(result)