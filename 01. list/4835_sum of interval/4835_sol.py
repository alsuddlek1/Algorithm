import sys
sys.stdin = open('input.txt')

# N개의 정수중에 연속된 M개의 최대,최소합의 차 수하기

# 데이터받기
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
# 연속된 M개의 정수

    maxV = 0
    minV = 100000
    for i in range(N-M+1):
        result = 0
        for j in range(i,i+M): # M개의 숫자 인덱스 뽑기
            # print(j) # 012,123,234,,,
            result += arr[j] # 정수의 합
# 최대, 최소값
        if result > maxV:
            maxV = result
        if result < minV:
            minV = result
    # print(maxV, minV)
# 결과
    results = maxV - minV
    print(f'#{tc} {results}')