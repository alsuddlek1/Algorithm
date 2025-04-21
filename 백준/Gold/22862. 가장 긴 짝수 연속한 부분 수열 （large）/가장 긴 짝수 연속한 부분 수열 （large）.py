import sys
input = sys.stdin.readline

# 0. 변수설정
N, K = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
odd_count = 0
result = 0


for end in range(N):
    # 1. 홀수 일 때
    if arr[end] % 2 == 1:
        odd_count += 1

    # 2. 홀수 개수가 K개 초과할 때
    while odd_count > K:
        if arr[start] % 2 ==1:
            odd_count -= 1
        start += 1

    # 3. 구간 내에서 짝수의 개수만 세기
    even_len = (end - start + 1) - odd_count
    result = max(result, even_len)

print(result)
