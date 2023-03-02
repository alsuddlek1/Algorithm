import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    data = list(map(int,input().split()))

    # N개중 내림차순정렬 후 K개 출력
    data.sort(reverse=True) # data를 내림차순으로 정렬
    # print(data)
    sub = []
    for i in range(K):
        sub.append(data[i]) # 높은 점수의 K개의 과목 점수
    # print(result)
    result = sum(sub) # K개의 과목 점수 합
    print(f'#{tc} {result}')