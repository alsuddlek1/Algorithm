import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int,input().split()))
    N = arr[0] # 학생수
    data = [] # N명의 점수
    for _ in range(1, len(arr)):
        data.append(arr[_])

    ave = sum(data) / N
    # print(ave)
    nn = []
    for i in range(len(data)):
        if data[i] > ave:
            nn.append(data[i])
    # print(nn)

    result = len(nn) / N * 100
    print(f'{format(result, ".3f")}%')