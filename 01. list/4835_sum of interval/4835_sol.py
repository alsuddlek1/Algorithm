import sys
sys.stdin = open('input.txt')

T = int(input()) # 테스트케이스 개수
for tc in range(1, T+1):
    N,M = map(int,input().split())
    # N : N개의 정수, 리스트 arr의 길이
    # M : 연속된 수의 개수, 연속된 수 M개의 합 구해야함
    arr = list(map(int, input().split()))
    # N개의 정수가 주어진 리스트


    maxV = 0
    minV = 10000
    for i in range(N-M+1):
        # i : arr의 인덱스
        # N-M+1 : M만큼 연속된 숫자의 수를 조사해야하므로 마지막 M개 빠짐
        sumV = 0  # M개의 이웃한 수의 합
        for j in range(i, i+M):
            # j : arr에서 M만큼의 인덱스
            # (i, i+3) : i부터 M만큼 조사
            sumV += arr[j]
            # arr[j]들의 합
            if sumV > maxV:
                maxV = sumV
            if sumV < minV:
                minV = sumV
    result = maxV - minV
    print(maxV, minV)
    print(result)