# 0. 변수설정
N, M = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(M):
    arr.sort()
    temp = arr[0] + arr[1]
    arr[0], arr[1] = temp, temp

result = sum(arr)
print(result)