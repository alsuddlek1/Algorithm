# 0. 변수 설정
n = int(input())
arr = list(map(int, input().split()))
mon = int(input())

# 1. 이분탐색 - mid 값이 상한 값 -> 합계가 예산 M 보다 작거나 같을 때 / 넘을 때
start = 0
end = max(arr)
answer = 0

while start <= end:
    mid = (start + end) // 2
    # print("s, e, m = ",start, end, mid)

    total = 0

    for i in arr:
        total += min(i, mid)
    # print(total)

    if total > mon:
        end = mid - 1
    else:
        answer = mid
        start = mid + 1

print(answer)