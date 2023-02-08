import sys
sys.stdin = open('sample_input.txt')
T = int(input())
number = list(map(int, input().split()))

N = number[0]
M = number[1]
for chars in range(N):
    chars = input()
    # print(chars)
    for i in range(M // 2):
        a = chars[i]
        b = chars[-i - 1]
        if a == b:
            print(chars)