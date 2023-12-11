import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    data = [input() for _ in range(5)] # 주어진 배열

    print(f'#{tc}', end=' ')
    for i in range(15):         # 문자열의 최대 길이 : 15
        for j in range(5):      # 문자열의 총 개수 : 5
            if i < len(data[j]):
                print(data[j][i], end='')
    print()