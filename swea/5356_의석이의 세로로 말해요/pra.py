import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    data = [list(input()) for _ in range(5)]

    arr = []
    for i in range(15): # 문자열 최대 길이가 15
        for j in range(5): # 문자열 다섯개
            if i < len(data[j]):
                arr.append(data[j][i])
    print(f'#{tc}', ''.join(arr))