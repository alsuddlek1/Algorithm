import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, input()))

    matrix = [0]*10
    max_count = 0
    max_value = 0
    for i in ai:
        matrix[i] += 1 # 방문 횟수마다 1 증가
        if max_count < matrix[i]:
            max_count = matrix[i] # 최대 방문
            max_value = i
        elif max_count == matrix[i] and max_value < i:
            max_count = matrix[i]
            max_value = i
