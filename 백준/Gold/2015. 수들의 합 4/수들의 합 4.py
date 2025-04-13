# 0. 변수설정
n, k = map(int, input().split())
arr = list(map(int, input().split()))
pre_sum = 0     # 누적함
pre_sums = {}   # 누적합 저장 딕셔너리
count = 0

# 1. 누적합 0일 때 부분합 K 방지
pre_sums[0]  = 1

# 2. 누적합 계산
for i in arr:
    pre_sum += i

    if (pre_sum - k) in pre_sums:
        count += pre_sums[pre_sum - k]

    if pre_sum in pre_sums:
        pre_sums[pre_sum] += 1
    else:
        pre_sums[pre_sum] = 1

###
print(count)
