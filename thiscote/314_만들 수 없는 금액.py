N = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1 # 최소 타겟
for i in data:
    if target < i:
        break
    else:
        target += i

print(target)