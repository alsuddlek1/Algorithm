import sys
sys.stdin = open('input.txt')

# N개의 정수가 들어있는 배열 중 이웃한 M개의 최대, 최소합의 차 출력

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # N : 정수의 개수
    # M : 구간의 길이
    data = list(map(int, input().split()))
    # N개의 정수로 이루어진 주어진 리스트

    maxV = 0        # 연속된 M개의 정수의 최대합 변수
    minV = sum(data)    # 연속된 M개의 정수의 최소합 변수,음수가 있을 수 있음
    for i in range(N-M+1):
    # i : N개의 정수로 이루어진 리스트의 인덱스
    # (N-M) : 연속된 수를 구해야 하므로 i가 N까지가 아닌 연속된 수 전까지인 N-M까지 조사
    # i = 0,1,2,3,4,5,6
    #     print(i)
        sumV = 0
        for j in range(i, i+M):
        # j : 연속된 M개의 N개의 정수로 이루어진 리스트의 이웃한 M개의 인덱스
        # j = 012, 123, 234, ,,,
        # (i, i+M) : i번째 인덱스부터 M개의 수를 조사
            sumV += data[j]
            # sumV에 M개의 이웃한 수 data[j]들을 더해준다
        if sumV > maxV:
            # sumV가 maxV보다 크다면 maxV에 sumV를 할당
            maxV = sumV
        if sumV < minV:
            # sumV가 minV보다 작다면 minV에 sumV를 할당
            minV = sumV
    # print(maxV, minV)

    result = maxV - minV
    print(f'#{tc} {result}')