import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    data = list(map(int, input().split())) # idx : 1~20 까지 학생
    t = data[0] # idx 번호

    res = 0
    for j in range(20): # 이 과정을 20번 반복함
        for i in range(1, 20): # 이 반복문은 가장 큰 수를 맨 뒤로 보내줌
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                res += 1

    print(f'{tc} {res}')
