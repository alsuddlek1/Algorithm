import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    number = list(map(int, input().split()))
    N = number[0]
    M = number[1]

    for char in range(N): # 문단
        chars = input().rstrip()

        for i in range(N - M + 1): #한문장씩 받아옴
            new_chars = chars[i:i+M]

            for j in range(M // 2): # 회문의 길이의 반만큼 길이 비교
                a = new_chars[j]
                b = new_chars[-j - 1]
