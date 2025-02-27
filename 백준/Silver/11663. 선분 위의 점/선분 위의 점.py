# 0. 변수설정
N, M = map(int, input().split()) # N : 점의 개수(len(array)) M : 선분개수
data = list(map(int, input().split()))
data.sort()

# 1. 이분탐색
## 1-1. lower - start 이상에서 처음 나오는 값
def lower_bound(arr, target):

    start, end = 0, len(arr)
    while start < end:
        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid
    return start

## 1-2. upper - end 이하에서 처음 나오는 값
def upper_bound(arr, target):
    start, end = 0, len(arr)
    while start < end:
        mid = (start + end) // 2
        if arr[mid] <= target:
            start = mid + 1
        else:
            end = mid
    return start

# 3. 호출
for i in range(M):
    # result = 0
    s, e = map(int, input().split())

    left_index = lower_bound(data,s)
    right_index = upper_bound(data, e)

    result = right_index - left_index

    print(result)